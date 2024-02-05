#!/usr/bin/python3
from models import storage
from api.v1.views import app_views
from flask import Flask
import os

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def close(error):
    storage.close()


if __name__ == '__main__':
    """Run the appplication"""
    # Define default values for host and port
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))

    # Run the Flask app with the specified parameters
    app.run(host=host, port=port, threaded=True)
    app.url_map.strict_slashes = False
