"""Module for defining routes."""

import json
from flask import jsonify, render_template, request, Response
import requests
from . import app

# This route can be altered later to request cat images in a specific order,
# depending on the functionality of the app
@app.route('/cat/images', methods=['GET'])
def cat_images():
    """Retrieve random cat images from the Cat API."""

    endpoint = '/images/search'
    api_url = f'{app.config["CAT_API_BASE_URL"]}{endpoint}'

    headers = {
        'Content-Type': 'application/json',
        'x-api-key': app.config['CAT_API_KEY']
    }

    # Define default values for parameters
    size = request.args.get('size', 'med')
    mime_types = request.args.get('mime_types', 'jpg')
    image_format = request.args.get('format', 'json')
    has_breeds = request.args.get('has_breeds', 'true')
    order = request.args.get('order', 'RANDOM')
    page = request.args.get('page', '0')
    limit = request.args.get('limit', '16')

    # Add parameters to the URL
    api_url += f'?size={size}&mime_types={mime_types}&format={image_format}' \
               f'&has_breeds={has_breeds}&order={order}&page={page}&limit={limit}'

    try:
        response = requests.get(api_url, headers=headers, timeout=30)

        response.raise_for_status()
        cat_data = response.json()
        formatted_data = json.dumps(cat_data, indent=2)

        return render_template('cats/cat_list.html', cat_data=cat_data)
        # return Response(response=formatted_data, content_type='application/json')
    except requests.RequestException as e:
        return jsonify({'error': f'Request failed: {str(e)}'}), 500

@app.route('/cat/images/<image_id>', methods=['GET'])
def get_cat_image_info(image_id):
    """Retrieve information about a specific cat image."""
    endpoint = f'/images/{image_id}'
    api_url = f'{app.config["CAT_API_BASE_URL"]}{endpoint}'

    headers = {
        'x-api-key': app.config['CAT_API_KEY']
    }

    try:
        response = requests.get(api_url, headers=headers, timeout=30)
        response.raise_for_status()
        image_info = response.json()

        formatted_data = json.dumps(image_info, indent=2)

        return render_template('cats/image_info.html', image_info=image_info)
        # return Response(response=formatted_data, content_type='application/json')
    except requests.RequestException as e:
        return jsonify({'error': f'Request failed: {str(e)}'}), 500

@app.route('/cat/breeds', methods=['GET'])
def get_cat_breeds():
    """Retrieve a list of cat breeds."""
    endpoint = '/breeds'
    api_url = f'{app.config["CAT_API_BASE_URL"]}{endpoint}'

    headers = {
        'Content-Type': 'application/json',
    }

    # Define default values for parameters
    limit = request.args.get('limit', '400')
    page = request.args.get('page', '0')

    # Add parameters to the URL
    api_url += f'?limit={limit}&page={page}'

    try:
        response = requests.get(api_url, headers=headers, timeout=30)
        response.raise_for_status()
        breeds_data = response.json()

        formatted_data = json.dumps(breeds_data, indent=2)

        return render_template('cats/cat_breeds.html', breeds_data=breeds_data)
        # return Response(response=formatted_data, content_type='application/json')
    except requests.RequestException as e:
        return jsonify({'error': f'Request failed: {str(e)}'}), 500

@app.route('/cat/breeds/<breed_id>', methods=['GET'])
def get_cat_breed_info(breed_id):
    """Retrieve information about a specific cat breed."""
    endpoint = f'/breeds/{breed_id}'
    api_url = f'{app.config["CAT_API_BASE_URL"]}{endpoint}'

    size = request.args.get('size', 'med')

    images_endpoint = f'/images/search?breed_id={breed_id}&limit=5&size={size}'
    images_api_url = f'{app.config["CAT_API_BASE_URL"]}{images_endpoint}'


    headers = {
        'Content-Type': 'application/json',
    }

    try:
        response = requests.get(api_url, headers=headers, timeout=30)
        response.raise_for_status()
        breed_info = response.json()

        images_response = requests.get(images_api_url, headers=headers, timeout=30)
        images_response.raise_for_status()
        images_info = images_response.json()

        formatted_data = json.dumps(breed_info, indent=2)

        return render_template('cats/breed_info.html', breed_info=breed_info, images_info=images_info,
                               next_breed_id=next_breed_id, prev_breed_id=prev_breed_id)
        # return Response(response=formatted_data, content_type='application/json')
    except requests.RequestException as e:
        return jsonify({'error': f'Request failed: {str(e)}'}), 500

@app.route('/cat/breeds/search', methods=['GET'])
def search_cat_breeds():
    """Search for cat breeds."""
    search_query = request.args.get('q', '')

    if not search_query:
        return jsonify({'error': 'Search query parameter "q" is required'}), 400

    endpoint = '/breeds/search'
    api_url = f'{app.config["CAT_API_BASE_URL"]}{endpoint}?q={search_query}'

    try:
        response = requests.get(api_url, timeout=30)
        response.raise_for_status()
        search_results = response.json()

        formatted_data = json.dumps(search_results, indent=2)

        # return render_template('breed_search_results.html', search_results=search_results)
        return Response(response=formatted_data, content_type='application/json')
    except requests.RequestException as e:
        return jsonify({'error': f'Request failed: {str(e)}'}), 500
