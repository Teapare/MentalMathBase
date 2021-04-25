import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase

association_table = sqlalchemy.Table(
    'formula_to_collection',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('formula', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('formulas.id')),
    sqlalchemy.Column('collection', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('collections.id'))
)


class Collection(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'collections'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True)
    name = sqlalchemy.Column(sqlalchemy.String)
