"""Module for defining routes."""

from flask import jsonify, render_template
import requests
from . import app

@app.route('/')
def home():
    """Render the home page."""
    return render_template('home.html')

@app.route('/dog/images')
def dog_images():
    """ The Dog API endpoint for random dog images"""

    endpoint = '/images/search'
    api_url = f'{app.config["DOG_API_BASE_URL"]}{endpoint}'

    headers = {
        'Content-Type': 'application/json',
        'x-api-key': app.config['DOG_API_KEY']
    }

    try:
        response = requests.get(api_url, headers=headers, timeout=10)

        response.raise_for_status()
        dog_data = response.json()
        return render_template('dog_images.html', dog_data=dog_data)
        
    except requests.RequestException as e:
        return jsonify({'error': f'Request failed: {str(e)}'}), 500
