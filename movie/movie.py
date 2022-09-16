from flask import Flask, render_template, jsonify, make_response, request
from pathlib import Path
import json

app = Flask(__name__)

with open(Path('.') / 'databases' / 'movies.json', 'r') as jsf:
    movies = json.load(jsf)['movies']


@app.route('/', methods=['GET'])
def index():
    return make_response(
        '<h1 style=\'color:blue\'>Welcome to the Movie service!</h1>', 200)


@app.route('/template', methods=['GET'])
def template():
    return make_response(
        render_template('index.html',
                        body_text='This is my HTML template for Movie service'),
        200)


@app.route('/json', methods=['GET'])
def get_json():
    res = make_response(jsonify(movies), 200)
    return res


@app.route('/movies/<movieid>', methods=['GET'])
def get_movie_byid(movieid):
    for movie in movies:
        if str(movie['id']) == str(movieid):
            res = make_response(jsonify(movie), 200)
            return res
    return make_response(jsonify({'error': 'Movie ID not found'}), 400)


@app.route('/movies/filtered', methods=['GET'])
def get_movies_filtered():
    if not request.args or 'rating' not in request.args:
        return make_response(jsonify({'error': 'No rating query parameter'}),
                             400)
    rating = request.args['rating']
    res = []
    for movie in movies:
        if float(movie['rating']) >= float(rating):
            res.append(movie)
    return make_response(jsonify({'movies': res}), 200)


@app.route('/titles', methods=['GET'])
def get_movie_bytitle():
    json_ = ''
    if request.args:
        req = request.args
        for movie in movies:
            if str(movie['title']) == str(req['title']):
                json_ = movie

    if not json_:
        res = make_response(jsonify({'error': 'movie title not found'}), 400)
    else:
        res = make_response(jsonify(json_), 200)
    return res


@app.route('/movies/<movieid>', methods=['POST'])
def create_movie(movieid):
    req = request.get_json()

    for movie in movies:
        if str(movie['id']) == str(movieid):
            return make_response(jsonify({'error': 'movie ID already exists'}),
                                 409)

    movies.append(req)
    res = make_response(jsonify({'message': 'movie added'}), 200)
    return res


@app.route('/movies/<movieid>/<rate>', methods=['PUT'])
def update_movie_rating(movieid, rate):
    for movie in movies:
        if str(movie['id']) == str(movieid):
            movie['rating'] = int(rate)
            res = make_response(jsonify(movie), 200)
            return res

    res = make_response(jsonify({'error': 'movie ID not found'}), 201)
    return res


@app.route('/movies/<movieid>', methods=['DELETE'])
def del_movie(movieid):
    for movie in movies:
        if str(movie['id']) == str(movieid):
            movies.remove(movie)
            return make_response(jsonify(movie), 200)

    res = make_response(jsonify({'error': 'movie ID not found'}), 400)
    return res


if __name__ == '__main__':
    from argparse import ArgumentParser
    arg_parser = ArgumentParser()
    arg_parser.add_argument('-H', '--host', required=False)
    arg_parser.add_argument('-p', '--port', type=int, required=True)
    args = arg_parser.parse_args()

    app.run(host=args.host, port=args.port)
