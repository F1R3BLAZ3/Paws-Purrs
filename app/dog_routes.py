"""
Module for defining routes related to the Dog API.
"""

import json
from flask import jsonify, render_template, request, Response
import requests
from . import app

@app.route('/')
def landing():
    """Render the landing page."""
    return render_template('landing.html')

@app.route('/home')
def home():
    """Render the home page.""" 
    return render_template('home.html')


# This route can be altered later to request dog images in a specific order,
# depending on the functionality of the app
@app.route('/dog/images', methods=['GET'])
def dog_images():
    """
    Retrieve random dog images from the Dog API.

    Returns:
    - HTML response rendering dog images in 'dogs/dog_list.html' template.
    - JSON response in case of a failure.
    """

    # Dog API endpoint for random images
    endpoint = '/images/search'
    api_url = f'{app.config["DOG_API_BASE_URL"]}{endpoint}'

    # Headers for the request
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': app.config['DOG_API_KEY']
    }

    # Define default values for parameters
    size = request.args.get('size', 'med')               # Image size
    mime_types = request.args.get('mime_types', 'jpg')   # MIME types
    image_format = request.args.get('format', 'json')    # Response format
    has_breeds = request.args.get('has_breeds', 'true')  # Include breeds information
    order = request.args.get('order', 'RANDOM')          # Order of images
    page = request.args.get('page', '0')                 # Page number
    limit = request.args.get('limit', '16')              # Number of images per page

    # Add parameters to the URL
    api_url += f'?size={size}&mime_types={mime_types}&format={image_format}' \
               f'&has_breeds={has_breeds}&order={order}&page={page}&limit={limit}'

    try:
        # Make a request to the Dog API
        response = requests.get(api_url, headers=headers, timeout=30)

        # Check if the request was successful
        response.raise_for_status()

        # Parse the JSON response
        dog_data = response.json()

        # Render the HTML template with the dog data
        return render_template('dogs/dog_list.html', dog_data=dog_data)

        # Alternatively, return a JSON response
        # formatted_data = json.dumps(dog_data, indent=2)
        # return Response(response=formatted_data, content_type='application/json')
    except requests.RequestException as e:
        # Return a JSON response in case of a failure
        return jsonify({'error': f'Request failed: {str(e)}'}), 500

@app.route('/dog/images/<image_id>', methods=['GET'])
def get_dog_image_info(image_id):
    """
    Retrieve information about a specific dog image.

    Args:
    - image_id (str): The unique identifier of the dog image.

    Returns:
    - HTML response rendering image information in 'dogs/dog_image_info.html' template.
    - JSON response in case of a failure.
    """

    # Dog API endpoint for a specific image
    endpoint = f'/images/{image_id}'
    api_url = f'{app.config["DOG_API_BASE_URL"]}{endpoint}'

    # Headers for the request
    headers = {
        'x-api-key': app.config['DOG_API_KEY']
    }

    try:
        # Make a request to the Dog API
        response = requests.get(api_url, headers=headers, timeout=30)

        # Check if the request was successful
        response.raise_for_status()

        # Parse the JSON response
        image_info = response.json()

        # Render the HTML template with the image information
        return render_template('dogs/dog_image_info.html', image_info=image_info)

        # Alternatively, return a JSON response
        # formatted_data = json.dumps(image_info, indent=2)
        # return Response(response=formatted_data, content_type='application/json')

    except requests.RequestException as e:
        # Return a JSON response in case of a failure
        return jsonify({'error': f'Request failed: {str(e)}'}), 500

@app.route('/dog/breeds', methods=['GET'])
def get_dog_breeds():
    """
    Retrieve a list of dog breeds.

    Returns:
    - HTML response rendering dog breeds in 'dogs/dog_breeds.html' template.
    - JSON response in case of a failure.
    """

    # Dog API endpoint for breeds
    endpoint = '/breeds'
    api_url = f'{app.config["DOG_API_BASE_URL"]}{endpoint}'

    # Headers for the request
    headers = {
        'Content-Type': 'application/json',
    }

    # Define default values for parameters
    limit = request.args.get('limit', '400')
    page = request.args.get('page', '0')

    # Add parameters to the URL
    api_url += f'?limit={limit}&page={page}'

    try:
        # Make a request to the Dog API
        response = requests.get(api_url, headers=headers, timeout=30)

        # Check if the request was successful
        response.raise_for_status()

        # Parse the JSON response
        breeds_data = response.json()

        # Render the HTML template with the breeds information
        return render_template('dogs/dog_breeds.html', breeds_data=breeds_data)

        # Alternatively, return a JSON response
        # formatted_data = json.dumps(breeds_data, indent=2)
        # return Response(response=formatted_data, content_type='application/json')
    except requests.RequestException as e:
        # Return a JSON response in case of a failure
        return jsonify({'error': f'Request failed: {str(e)}'}), 500


@app.route('/dog/breeds/<int:breed_id>', methods=['GET'])
def get_breed_info(breed_id):
    """
    Retrieve information about a specific dog breed.

    Args:
    - breed_id (int): The unique identifier of the dog breed.

    Returns:
    - HTML response rendering dog breed information in 'dogs/dog_breed_info.html' template.
    - JSON response in case of a failure.
    """

    # Dog API endpoint for breed information
    endpoint = f'/breeds/{breed_id}'
    api_url = f'{app.config["DOG_API_BASE_URL"]}{endpoint}'

    # Default size for images
    size = request.args.get('size', 'med')

    # Dog API endpoint for breed images
    images_endpoint = f'/images/search?breed_id={breed_id}&limit=5&size={size}'
    images_api_url = f'{app.config["DOG_API_BASE_URL"]}{images_endpoint}'

    # Headers for the request
    headers = {
        'Content-Type': 'application/json',
    }

    try:
        # Request breed information from the Dog API
        response = requests.get(api_url, headers=headers, timeout=30)

        # Check if the request was successful
        response.raise_for_status()

        # Parse the JSON response for breed information
        breed_info = response.json()

        # Request breed images from the Dog API
        images_response = requests.get(images_api_url, headers=headers, timeout=30)

        # Check if the request for images was successful
        images_response.raise_for_status()

        # Parse the JSON response for breed images
        images_info = images_response.json()

        # Render the HTML template with breed information and images
        next_breed_id = breed_id + 1
        prev_breed_id = breed_id - 1 if breed_id > 1 else None
        return render_template('dogs/dog_breed_info.html', breed_info=breed_info,
                               images_info=images_info, next_breed_id=next_breed_id,
                               prev_breed_id=prev_breed_id)

        # Alternatively, return a JSON response
        # formatted_data = json.dumps(breed_info, indent=2)
        # return Response(response=formatted_data, content_type='application/json')
    except requests.RequestException as e:
        # Return a JSON response in case of a failure
        return jsonify({'error': f'Request failed: {str(e)}'}), 500


@app.route('/dog/breeds/search', methods=['GET'])
def search_dog_breeds():
    """
    Search for dog breeds.

    Returns:
    - JSON response containing search results or
    - JSON response in case of a failure.
    """

    # Retrieve the search query from the request parameters
    search_query = request.args.get('q', '')

    # Check if the search query is provided
    if not search_query:
        return jsonify({'error': 'Search query parameter "q" is required'}), 400

    # Dog API endpoint for searching dog breeds
    endpoint = '/breeds/search'
    api_url = f'{app.config["DOG_API_BASE_URL"]}{endpoint}?q={search_query}'

    try:
        # Request to the Dog API for searching dog breeds
        response = requests.get(api_url, timeout=30)

        # Check if the request was successful
        response.raise_for_status()

        # Parse the JSON response for search results
        search_results = response.json()

        # Convert the search results to a formatted JSON string
        formatted_data = json.dumps(search_results, indent=2)

        # Render the HTML template with search results
        # return render_template('breed_search_results.html', search_results=search_results)

        # Alternatively, return a JSON response
        return Response(response=formatted_data, content_type='application/json')
    except requests.RequestException as e:
        # Return a JSON response in case of a failure
        return jsonify({'error': f'Request failed: {str(e)}'}), 500

