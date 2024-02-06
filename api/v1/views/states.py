#!/usr/bin/python3
'''States endpoint'''
from flask import Flask, jsonify, abort, make_response, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
@app_views.route('/states/<state_id>', methods=['GET'],
                 strict_slashes=False)
def state_view(state_id=None):
    '''Endpoint to get all states'''
    all_states = storage.all(State).values()
    if state_id:
        res = [state for state in all_states if state.id == state_id]
        if res:
            return jsonify(res[0].to_dict())
        abort(404)
    return jsonify([state.to_dict() for state in all_states])


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    '''Delete a state'''
    state = storage.get(State, state_id)
    if state:
        storage.delete(state)
        storage.save()
        return make_response(jsonify({}), 200)
    abort(404)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    '''Create a new state of specified id with the request json'''
    data = request.get_json()
    if type(data) is not dict:
        abort(400, 'Not a JSON')
    if 'name' not in data:
        abort(404, 'Missing name')
    state = State(**data)
    storage.new(state)
    storage.save()
    return make_response(jsonify(state.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    '''Update state with state_id'''
    state = storage.get(State, state_id)
    data = request.get_json()
    if type(data) is not dict:
        abort(400, 'Not a JSON')
    if state:
        for key, value in data.items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(state, key, value)
        storage.save()
        return make_response(jsonify(state.to_dict()), 200)
    abort(404)
