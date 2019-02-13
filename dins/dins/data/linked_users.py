import datetime
import sqlalchemy as sa
from dins.data.modelbase import SqlAlchemyBase


class Link(SqlAlchemyBase):
    __tablename__ = 'linked'

    chef_id = sa.Column(sa.Integer)
    diner_id = sa.Column(sa.Integer, primary_key=True)
