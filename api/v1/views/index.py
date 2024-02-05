#!/usr/bin/python3
"""Returns a status route"""
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status')
def get_status():
    """Returns status json"""
    stat = {
        'status': 'OK'
    }
    return jsonify(stat)

@app_views.route('/stats')
def show_stats():
    """Returns the number of objects by type"""
    stats = {
        'amenities': storage.count(Amenity),
        'cities': storage.count(City),
        'places': storage.count(Place),
        'reviews': storage.count(Review),
        'states': storage.count(State),
        'users': storage.count(User),
    }
    return jsonify(stats)