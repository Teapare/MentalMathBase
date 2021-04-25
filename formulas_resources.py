from data import db_session
from flask import jsonify
from data.formulas import Formula
from flask_restful import Resource, abort


def abort_if_formula_not_found(formula_id):
    session = db_session.create_session()
    formula = session.query(Formula).get(formula_id)
    if not formula:
        abort(404, message=f"Formula {formula_id} not found")


class FormulaResource(Resource):
    def get(self, formula_id):
        abort_if_formula_not_found(formula_id)
        session = db_session.create_session()
        formula = session.query(Formula).get(formula_id)
        return jsonify({'formula': formula.to_dict(only=())})