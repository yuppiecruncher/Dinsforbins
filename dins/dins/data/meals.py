import datetime
import sqlalchemy as sa
from dins.data.modelbase import SqlAlchemyBase


class Meal(SqlAlchemyBase):
    __tablename__ = 'meals'

    id = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now)
    meal_avail_date = sa.Column(sa.DateTime, index=True)
    meal_title = sa.Column(sa.String)
    meal_description = sa.Column(sa.String)


    # reference for debugging in editor
    def __repr__(self):
        return '<Package {}>'.format(self.id)
