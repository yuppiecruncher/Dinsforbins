import datetime
import sqlalchemy as sa
from dins.data.modelbase import SqlAlchemyBase


class ReqMeal(SqlAlchemyBase):
    __tablename__ = 'requested_meals'

    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"), primary_key=True, nullable=False)
    req_date = sa.Column(sa.DateTime, default=datetime.datetime.now)
    meal_avail_date = sa.Column(sa.DateTime, index=True)
    meal_title = sa.Column(sa.String)
    meal_description = sa.Column(sa.String)
    chef_id = sa.Column(sa.Integer)
    diner_id = sa.Column(sa.Integer)
