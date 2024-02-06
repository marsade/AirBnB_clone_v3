#!/usr/bin/python3
'''Amenities endpoint'''
from flask import Flask, jsonify, abort, make_response, request
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity


@app_views.route('/amenitites', methods=['GET'],
                 strict_slashes=False)
@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def amenity_view(amenity_id=None):
    '''Endpoint to get all states'''
    all_amenities = storage.all(Amenity).values()
    if amenity_id:
        res = [amenity for amenity in all_amenities if amenity.id == amenity_id]
        if res:
            return jsonify(res[0].to_dict())
        abort(404)
    return jsonify([state.to_dict() for state in all_amenities])


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_amenity(amenity_id):
    '''Delete an amenity'''
    amenity = storage.get(Amenity, amenity_id)
    if amenity:
        storage.delete(amenity)
        storage.save()
        return make_response(jsonify({}), 200)
    abort(404)


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_amenity():
    '''Create a new state of specified id with the request json'''
    data = request.get_json()
    if type(data) is not dict:
        abort(400, 'Not a JSON')
    if 'name' not in data:
        abort(404, 'Missing name')
    amenity = Amenity(**data)
    storage.new(amenity)
    storage.save()
    return make_response(jsonify(amenity.to_dict()), 201)


@app_views.route('/amenities/<amenity_id>', methods=['PUT'], strict_slashes=False)
def update_amenity(amenity_id):
    '''Update amenity with amenity_id'''
    amenity = storage.get(Amenity, amenity_id)
    data = request.get_json()
    if type(data) is not dict:
        abort(400, 'Not a JSON')
    if amenity:
        for key, value in data.items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(amenity, key, value)
        storage.save()
        return make_response(jsonify(amenity.to_dict()), 200)
    abort(404)

