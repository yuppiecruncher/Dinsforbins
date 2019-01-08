from dins import DbSession
from typing import *
from dins.data.meals import Meal

def meal_title():
    session = DbSession.factory()
    query = session.query(Meal.meal_title)
    for row in query:
        return (row._asdict())

# def meal_title() -> str:
#     session = DbSession.factory()
#
#     meals = session.query(Meal)
#
#     meal_titles_list = {m.meal_title for m in meals}
#
#     for m in meals:
#         return meal_titles_list
