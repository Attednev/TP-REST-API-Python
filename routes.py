from flask import jsonify, request
import json
from i_o_handler import get_json_content, write_json_content
from flask_handler import app, build_message


@app.route('/')
def default_request():
    return jsonify({"all_movies_url": request.base_url + "movies", "all_rooms_url": request.base_url + "rooms",
                    "movie_url": request.base_url + "movies/{movie}", "rooms_url": request.base_url + "room/{room}",
                    "create_movie_url": request.base_url + "create/movie"})


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"message": "Not Found", "documentation_url": request.base_url}), 404


@app.route('/rooms')
def get_rooms():
    return build_message("rooms", get_json_content("Rooms"), "id"), 201


@app.route('/movies')
def get_movies():
    return build_message("movies", get_json_content("Movies"), "name"), 201


@app.route('/movies/<string:name>')
def get_movie_information(name):
    try:
        return build_message("movie", get_json_content("Movies", name, "name")), 201
    except IOError:
        return jsonify({"message": "This movie in not played", "documentation": request.base_url}), 404


@app.route('/rooms/<string:room_id>')
def get_room_information(room_id):
    try:
        return build_message("room", get_json_content("Rooms", room_id, "id")), 201
    except IOError:
        return jsonify({"message": "This room does not exist", "documentation": request.base_url}), 404


@app.route('/create/movie', methods=['POST', 'GET'])
def create_movie():
    print(request.method)
    if request.method == 'POST':
        file_data = get_json_content("Movies")
        json_data = json.loads(request.data)
        if 'movie' in json_data:
            file_data.append(json_data['movie'])
            write_json_content("Movies", file_data)
            return jsonify({"message": "The movie was successfully created", "documentation_url": request.base_url}), 201
        else:
            return jsonify({"message": "Request body is invalid", "documentation_url": request.base_url}), 400
    return jsonify({"message": "GET is not valid for this request", "documentation_url": request.base_url}), 400
