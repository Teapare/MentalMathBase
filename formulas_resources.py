from data import db_session
from flask import jsonify
from data.formulas import Formula
from flask_restful import Resource, abort
from formulas_reqparse import parser


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
        res = {'formula': formula.to_dict(only=('name', 'essentials', 'id'))}
        res['formula']['collections'] = [li.id for li in formula.collections]
        return jsonify(res)

    def delete(self, formula_id):
        abort_if_formula_not_found(formula_id)
        session = db_session.create_session()
        formula = session.query(Formula).get(formula_id)
        session.delete(formula)
        session.commit()
        return jsonify({'success': 'OK'})

class FormulaListResource(Resource):
    def get(self):
        session = db_session.create_session()
        formulas = session.query(Formula).all()
        res = {'formulas': [item.to_dict(only=('name', 'essentials', 'id')) for item in formulas]}
        res['formulas'] = []
        for item in formulas:
            d = item.to_dict(only=('name', 'essentials', 'id'))
            d['lists'] = [li.id for li in item.collections]
            res['formulas'].append(d)
        return jsonify(res)

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        formula = Formula(name=args['name'], essentials=args['essentials'])
        session.add(formula)
        session.commit()
        return jsonify({'success': 'OK'})