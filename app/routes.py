"""Module for defining routes."""

from flask import jsonify
import requests
from . import app

# Define a route to get dog data from The Dog API


@app.route('/get_dog_images')
def get_dog_images():
    """ The Dog API endpoint for random dog images"""
    api_url = 'https://api.thedogapi.com/v1/images/search'
    api_key = 'live_GeBIeu68rG3NZNLry3widTrMlCgl9k24TlDGFg0unSRs4geCUXqq5gIL1oqG9ILs'

    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key
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
