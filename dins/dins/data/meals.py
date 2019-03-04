import datetime
import sqlalchemy as sa
from dins.data.modelbase import SqlAlchemyBase


class Meal(SqlAlchemyBase):
    __tablename__ = 'meals'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now)
    meal_avail_date = sa.Column(sa.DateTime, index=True)
    meal_title = sa.Column(sa.String)
    meal_description = sa.Column(sa.String)
    chef_id = sa.Column(sa.Integer)
    diner_id = sa.Column(sa.Integer)
    requested_by_diner = sa.Column(sa.Integer) #diner_services will break with removal.
