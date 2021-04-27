import json

from flask import Flask, render_template
from flask_restful import reqparse, abort, Api, Resource

import collections_resources
from data import db_session
import formulas_resources
from data.formulas import Formula
from data.collections import Collection

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = "Hello"


@app.route('/')
def index():
    return render_template('index.html')


def main():
    db_session.global_init("db/formulas.db")
    api.add_resource(formulas_resources.FormulaListResource, '/api/v2/formulas')
    api.add_resource(formulas_resources.FormulaResource, '/api/v2/formulas/<int:formula_id>')
    api.add_resource(collections_resources.CollectionResource, '/api/v2/collections/<int:collection_id>')
    api.add_resource(collections_resources.CollectionListResource, '/api/v2/collections')
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
