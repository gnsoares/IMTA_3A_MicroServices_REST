from flask import Flask, render_template, request, jsonify, make_response
import json
from werkzeug.exceptions import NotFound

app = Flask(__name__)

with open('{}/databases/times.json'.format('.'), 'r') as jsf:
    schedule = json.load(jsf)['schedule']


@app.route('/', methods=['GET'])
def home():
    return '<h1 style=\'color:blue\'>Welcome to the Showtime service!</h1>'


@app.route('/showtimes', methods=['GET'])
def get_schedule():
    return make_response(jsonify(schedule), 200)


@app.route('/showmovies/<date>', methods=['GET'])
def get_movies_bydate(date):
    for schedule_date in schedule:
        if schedule_date['date'] == date:
            return make_response(jsonify(schedule_date), 200)
    return make_response(jsonify({'error': 'bad input parameter'}), 400)


if __name__ == '__main__':
    from argparse import ArgumentParser
    arg_parser = ArgumentParser()
    arg_parser.add_argument('-H', '--host', required=False)
    arg_parser.add_argument('-p', '--port', type=int, required=True)
    args = arg_parser.parse_args()

    print('Server running in port %s' % (args.port))
    app.run(host=args.host, port=args.port)
