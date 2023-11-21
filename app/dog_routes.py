"""Module for defining routes."""

import json
from flask import jsonify, render_template, request, Response
import requests
from . import app

@app.route('/')
def home():
    """Render the home page."""
    return render_template('home.html')

# This route can be altered later to request dog images in a specific order,
# depending on the functionality of the app
@app.route('/dog/images', methods=['GET'])
def dog_images():
    """The Dog API endpoint for random dog images"""

    endpoint = '/images/search?size=med'
    api_url = f'{app.config["DOG_API_BASE_URL"]}{endpoint}'

    headers = {
        'Content-Type': 'application/json',
        'x-api-key': app.config['DOG_API_KEY']
    }

    try:
        response = requests.get(api_url, headers=headers, timeout=10)

        response.raise_for_status()
        dog_data = response.json()

        formatted_data = json.dumps(dog_data, indent=2)

        #return render_template('dog_images.html', dog_data=dog_data)
        return Response(response=formatted_data, content_type='application/json')
    except requests.RequestException as e:
        return jsonify({'error': f'Request failed: {str(e)}'}), 500

@app.route('/dog/images/<image_id>', methods=['GET'])
def get_dog_image_info(image_id):
    """Route for getting information about a specific dog image"""
    endpoint = f'/images/{image_id}'
    api_url = f'{app.config["DOG_API_BASE_URL"]}{endpoint}'

    headers = {
        'x-api-key': app.config['DOG_API_KEY']
    }

    try:
        response = requests.get(api_url, headers=headers, timeout=10)
        response.raise_for_status()
        image_info = response.json()

        formatted_data = json.dumps(image_info, indent=2)

        # return render_template('image_info.html', image_info=image_info)
        return Response(response=formatted_data, content_type='application/json')
    except requests.RequestException as e:
        return jsonify({'error': f'Request failed: {str(e)}'}), 500

@app.route('/dog/images/<image_id>/analysis', methods=['GET'])
def analyze_dog_image(image_id):
    """Route for analyzing a specific dog image"""
    endpoint = f'/images/{image_id}/analysis'
    api_url = f'{app.config["DOG_API_BASE_URL"]}{endpoint}'

    headers = {
        'x-api-key': app.config['DOG_API_KEY']
    }

    try:
        response = requests.get(api_url, headers=headers, timeout=10)
        response.raise_for_status()
        analysis_data = response.json()

        formatted_data = json.dumps(analysis_data, indent=2)

        # return render_template('image_analysis.html', analysis_data=analysis_data)
        return Response(response=formatted_data, content_type='application/json')
    except requests.RequestException as e:
        return jsonify({'error': f'Request failed: {str(e)}'}), 500

@app.route('/dog/images/<image_id>/breeds', methods=['GET'])
def get_dog_image_breeds(image_id):
    """Route for getting breeds associated with a specific dog image"""
    endpoint = f'/images/{image_id}/breeds'
    api_url = f'{app.config["DOG_API_BASE_URL"]}{endpoint}'

    headers = {
        'Content-Type': 'application/json',
    }

    try:
        response = requests.get(api_url, headers=headers, timeout=10)
        response.raise_for_status()
        breeds_data = response.json()

        formatted_data = json.dumps(breeds_data, indent=2)

        # return render_template('image_breeds.html', breeds_data=breeds_data)
        return Response(response=formatted_data, content_type='application/json')
    except requests.RequestException as e:
        return jsonify({'error': f'Request failed: {str(e)}'}), 500

@app.route('/dog/images/random', methods=['GET'])
def get_random_dog_images():
    """Route for getting random dog images"""
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

        formatted_data = json.dumps(dog_data, indent=2)

        # return render_template('dog_images.html', dog_data=dog_data)
        return Response(response=formatted_data, content_type='application/json')
    except requests.RequestException as e:
        return jsonify({'error': f'Request failed: {str(e)}'}), 500

@app.route('/dog/breeds', methods=['GET'])
def get_dog_breeds():
    """Route for getting a list of breeds"""
    endpoint = '/breeds'
    api_url = f'{app.config["DOG_API_BASE_URL"]}{endpoint}'

    headers = {
        'Content-Type': 'application/json',
    }

    try:
        response = requests.get(api_url, headers=headers, timeout=10)
        response.raise_for_status()
        breeds_data = response.json()

        formatted_data = json.dumps(breeds_data, indent=2)

        # return render_template('breeds.html', breeds_data=breeds_data)
        return Response(response=formatted_data, content_type='application/json')
    except requests.RequestException as e:
        return jsonify({'error': f'Request failed: {str(e)}'}), 500

@app.route('/dog/breeds/<breed_id>', methods=['GET'])
def get_breed_info(breed_id):
    """Route for getting information about a specific breed"""
    endpoint = f'/breeds/{breed_id}'
    api_url = f'{app.config["DOG_API_BASE_URL"]}{endpoint}'

    headers = {
        'Content-Type': 'application/json',
    }

    try:
        response = requests.get(api_url, headers=headers, timeout=10)
        response.raise_for_status()
        breed_info = response.json()

        formatted_data = json.dumps(breed_info, indent=2)

        # return render_template('breed_info.html', breed_info=breed_info)
        return Response(response=formatted_data, content_type='application/json')
    except requests.RequestException as e:
        return jsonify({'error': f'Request failed: {str(e)}'}), 500

@app.route('/dog/breeds/search', methods=['GET'])
def search_dog_breeds():
    """Route for searching dog breeds"""
    search_query = request.args.get('q', '')  # Get the search query from the URL parameter 'q'

    # If the search query is empty, return an error response
    if not search_query:
        return jsonify({'error': 'Search query parameter "q" is required'}), 400

    endpoint = '/breeds/search'
    api_url = f'{app.config["DOG_API_BASE_URL"]}{endpoint}?q={search_query}'

    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        search_results = response.json()

        formatted_data = json.dumps(search_results, indent=2)

        # return render_template('breed_search_results.html', search_results=search_results)
        return Response(response=formatted_data, content_type='application/json')
    except requests.RequestException as e:
        return jsonify({'error': f'Request failed: {str(e)}'}), 500
