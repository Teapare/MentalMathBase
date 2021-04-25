import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class FormulaList(SqlAlchemyBase):
    __tablename__ = 'lists'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True)
    instances = orm.relation('Instance', back_populates='formula_list')