"""Module for defining routes."""

from flask import jsonify
import requests
from . import app


@app.route('/get_dog_images')
def get_dog_images():
    """ The Dog API endpoint for random dog images"""

    endpoint = '/images/search'
    api_url = f'{app.config["DOG_API_BASE_URL"]}{endpoint}'

    headers = {
        'Content-Type': 'application/json',
        'x-api-key': app.config['DOG_API_KEY']
    }

    try:
        response = requests.get(api_url, headers=headers, timeout=10)

        if response.status_code == 200:
            dog_data = response.json()
            return jsonify(dog_data)
        return jsonify(
                {'error': f'Failed to fetch dog data. Status code: {response.status_code}'}
            ), 500
    except requests.RequestException as e:
        return jsonify({'error': f'Request failed: {str(e)}'}), 500
