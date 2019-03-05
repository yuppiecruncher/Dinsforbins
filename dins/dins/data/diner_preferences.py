import datetime
import sqlalchemy as sa
from dins.data.modelbase import SqlAlchemyBase


class DinerPreference(SqlAlchemyBase):
    __tablename__ = 'preferences'

    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"), primary_key=True, nullable=False)
    allergies = sa.Column(sa.String)
    dislikes = sa.Column(sa.String)
    diet = sa.Column(sa.String)
