import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Instance(SqlAlchemyBase):
    __tablename__ = 'instances'
    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True, unique=True)
    formula_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('formulas.id'))
    formula = orm.relation('Formula')
    list_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('lists.id'))
    formula_list = orm.relation('FormulaList')