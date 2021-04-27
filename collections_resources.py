from data import db_session
from flask import jsonify
from data.collections import Collection
from flask_restful import Resource, abort
from collections_reqparse import parser
from json import loads
from data.formulas import Formula


def abort_if_collection_not_found(collection_id):
    session = db_session.create_session()
    collection = session.query(Collection).get(collection_id)
    if not collection:
        abort(404, message=f"List {collection_id} not found")


class CollectionResource(Resource):
    def get(self, collection_id):
        abort_if_collection_not_found(collection_id)
        session = db_session.create_session()
        collection = session.query(Collection).get(collection_id)
        res = {'collection': collection.to_dict(only=('name', 'id'))}
        res['collection']['formulas'] = [formula.id for formula in collection.formulas]
        return jsonify(res)

    def delete(self, collection_id):
        abort_if_collection_not_found(collection_id)
        session = db_session.create_session()
        collection = session.query(Collection).get(collection_id)
        session.delete(collection)
        session.commit()
        return jsonify({'success': 'OK'})

class CollectionListResource(Resource):
    def get(self):
        session = db_session.create_session()
        collections = session.query(Collection).all()
        # res = {'collections': [item.to_dict(only=('name', 'id')) for item in collections]}
        res = {'collections': []}
        for item in collections:
            d = item.to_dict(only=('name', 'id'))
            d['formulas'] = [formula.id for formula in item.formulas]
            res['collections'].append(d)
        return jsonify(res)

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        formulas = loads(args['formulas'])
        collection = Collection(name=args['name'])
        print(formulas)
        for i in formulas:
            collection.formulas.append(session.query(Formula).get(i))
        session.add(collection)
        session.commit()
        return jsonify({'success': 'OK'})