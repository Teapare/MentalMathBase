import sqlalchemy
from sqlalchemy.sql import sqltypes
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Formula(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'formulas'
    name = sqlalchemy.Column(sqlalchemy.String)
    essentials = sqlalchemy.Column(sqltypes.JSON)
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True)
    collections = orm.relation('Collection', secondary='formula_to_collection', backref='formulas')

