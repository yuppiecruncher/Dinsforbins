from dins import DbSession
from typing import *
from dins.data.meals import Meal
from dins.data.users import User
import datetime


####################### QUERY DINER MEALS FOR THE WEEK ####################################################
# def get_diner_meals(user_id: int):
#     session = DbSession.factory()
#
#     meals_query = session.query(Meal).filter(Meal.diner_id == user_id)
#
#     titles = [t.meal_title for t in meals_query]
#     description = [d.meal_description for d in meals_query]
#
#     return titles, description






def meal_title(d_id):
    session = DbSession.factory()

    meals = session.query(Meal).filter(Meal.diner_id == d_id)
    meal_titles_list = [m.meal_title for m in meals]

    for m in meal_titles_list:
        return meal_titles_list

def meal_desc(d_id):
    session = DbSession.factory()

    descriptions = session.query(Meal).filter(Meal.diner_id == d_id)

    description_list = [m.meal_description for m in descriptions]

    for m in description_list:
        return description_list

def meal_date(d_id):
    session = DbSession.factory()

    date_query = session.query(Meal).filter(Meal.diner_id == d_id)

    date_list = [m.meal_avail_date for m in date_query]

    # for m in date_list:
    #     formatted_date_list = date_list

    for m in date_list:
        return date_list

def get_diner_meals(user_id: int):
    d_id = user_id
    titles = meal_title(d_id)
    desc = meal_desc(d_id)
    date = meal_date(d_id)
    if not titles or not desc or not date:
        return None

    return [
        {'name': titles[0], 'description': desc[0], 'date': date[0].strftime("%A, %B, %d"),},
        {'name': titles[1], 'description': desc[1], 'date': date[1].strftime("%A, %B, %d"),},
        {'name': titles[2], 'description': desc[2], 'date': date[2].strftime("%A, %B, %d"),},
    ]
