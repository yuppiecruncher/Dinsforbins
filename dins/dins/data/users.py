import datetime
import sqlalchemy as sa
from dins.data.modelbase import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, index=True, unique=True)
    hashed_password = sa.Column(sa.String, index=True)
    role = sa.Column(sa.String, index=True)

    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now)
    last_login = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
