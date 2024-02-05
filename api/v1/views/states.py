#!/usr/bin/python3
from flask import Flask, jsonify, abort
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'])
@app_views.route('/states/', methods=['GET'])
@app_views.route('/states/<state_id>', methods=['GET'])
@app_views.route('/states/<state_id>/', methods=['GET'])
def state_view(state_id=None):
    '''Endpoint to get all states'''
    all_states = storage.all(State).values()
    if state_id:
        res = [state for state in all_states if state.id == state_id]
        if res:
            return jsonify(res[0].to_dict())
        abort(404)
    return jsonify([state.to_dict() for state in all_states])


@app_views.route('/states/<state_id>', methods=['DELETE'])
@app_views.route('/states/<state_id>/', methods=['DELETE'])
def delete_state(state_id):
    '''Delete a state'''
    all_states = storage.all(State).values()
    res = [state for state in all_states if state.id == state_id]
    if res:
        storage.delete(res[0])
        storage.save()
        return jsonify({}, 200)
    abort(404)
