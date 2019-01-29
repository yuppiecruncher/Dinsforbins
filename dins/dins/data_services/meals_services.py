from dins import DbSession
from typing import *
from dins.data.meals import Meal
from datetime import datetime

####################### ADD MEALS TO DB ####################################################

def create_meal(title: str, menudescription: str, available: str) -> Meal:
    meal = Meal()
    meal.meal_title = title
    meal.meal_description = menudescription
    date_input = available
    year, month, day = map(int, date_input.split('-'))
    date1 = datetime.date(year, month, day)
    meal.meal_avail_date = date1

    session = DbSession.factory()
    session.add(meal)
    session.commit()

    return meal

####################### QUERY MEALS FOR DISPLAY ####################################################
def meal_title():
    session = DbSession.factory()

    meals = session.query(Meal).order_by(Meal.meal_avail_date.desc())

    meal_titles_list = [m.meal_title for m in meals]

    for m in meal_titles_list:
        return meal_titles_list

def meal_desc():
    session = DbSession.factory()

    descriptions = session.query(Meal).order_by(Meal.meal_avail_date.desc())

    description_list = [m.meal_description for m in descriptions]

    for m in description_list:
        return description_list

def meal_date():
    session = DbSession.factory()

    date_query = session.query(Meal).order_by(Meal.meal_avail_date.desc())

    date_list = [m.meal_avail_date for m in date_query]

    # for m in date_list:
    #     formatted_date_list = date_list

    for m in date_list:
        return date_list

def get_meals():
    titles = meal_title()
    desc = meal_desc()
    date = meal_date()
    return [
        {'name': titles[0], 'description': desc[0], 'date': date[0].strftime("%A, %B, %d"),},
        {'name': titles[1], 'description': desc[1], 'date': date[1].strftime("%A, %B, %d"),},
        {'name': titles[2], 'description': desc[2], 'date': date[2].strftime("%A, %B, %d"),},
    ]
