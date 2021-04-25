import sqlalchemy
from sqlalchemy.sql import sqltypes
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Formula(SqlAlchemyBase):
    __tablename__ = 'formulas'
    name = sqlalchemy.Column(sqlalchemy.String)
    essentials = sqlalchemy.Column(sqltypes.JSON)
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True)
    instances = orm.relation('Instance', back_populates='formula')