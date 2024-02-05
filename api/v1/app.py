#!/usr/bin/python3
"""Run Flask application"""
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close(error):
    """close app context"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    response = {
        'error': 'Not found',
    }
    return jsonify(response), 404


if __name__ == '__main__':
    """Run the appplication"""
    # Define default values for host and port
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))

    # Run the Flask app with the specified parameters
    app.run(host=host, port=port, threaded=True)
    app.url_map.strict_slashes = False
