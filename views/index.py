from flask import render_template, jsonify, request, abort, redirect, url_for
from . import library
from scripts import fake_amel


@library.route('/')
def index():
    return render_template('index.html')


@library.route('/amelinium', methods=['GET'])
def amelinium():
    return render_template('amelinium.html')


@library.route('/people', methods=['GET'])
def json_sandbox():

    def validate_parameters(n):
        try:
            populate_n = int(n)
        except (TypeError, ValueError):
            abort(400)
        return populate_n

    if request.method == 'GET':
        population = validate_parameters(request.args.get('n', None))
        if population == 0:
            return redirect(url_for('library.index'), code=302)

        fake_j = fake_amel.fake_json(population)
        return jsonify(fake_j)
