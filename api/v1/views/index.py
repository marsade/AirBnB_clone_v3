#!/usr/bin/python3
"""Returns a status route"""
from api.v1.views import app_views
from flask import Flask, jsonify


@app_views.route('/status')
def get_status():
    stat = {
        'status': 'OK'
    }
    return jsonify(stat)
