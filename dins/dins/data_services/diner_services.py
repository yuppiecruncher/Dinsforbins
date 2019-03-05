from dins import DbSession
from typing import *
from dins.data.meals import Meal
from dins.data.users import User
import datetime
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

################## ADD REQUEST TO DB #####################################################

def request_meal(title: str, menudescription: str, available: str, user_id: int, chef_email: str) -> Meal:
    session = DbSession.factory()
    meal = Meal()
    meal.meal_title = title
    meal.meal_description = menudescription
    date_input = available
    year, month, day = map(int, date_input.split('-'))
    date1 = datetime.date(year, month, day)

    #### DUPLICATE MEAL CHECK ####
    # Not currently working correctly
    # duplicate = session.query(Meal).filter(Meal.meal_avail_date == date1)
    # if duplicate:
    #     return None

    meal.meal_avail_date = date1
    meal.diner_id = user_id
    #REMOVED THIS FROM TABLE################################
    meal.requested_by_diner = user_id

    #### chef_email to chef_id conversion ####
    email = chef_email.lower().strip()
    user = session.query(User).filter(User.email == email).first()
    if not user:
        return None
    chef_id = user.id
    ########                  ############

    meal.chef_id = chef_id
    session.add(meal)
    session.commit()

    return meal

def chef_validation(chef_email: str):
        session = DbSession.factory()
        email = chef_email.lower().strip()
        user = session.query(User).filter(User.email == email).first()
        if not user:
            return None

        return user
################## QUERY CHEF FOR DISPLAY #####################################################


################## QUERY FOR WEEKLY MEALS BY DAY #####################################################
def date_today():
    today = datetime.datetime.now()
    today = today.replace(hour=0, minute=0, second=0, microsecond=0)
    return today

def query_today(user_id: int):
    day = date_today()
    session = DbSession.factory()
    #TODO: Implement error handling for multiple results on same day if chef makes two meals available on same day
    row_day = session.query(Meal).filter(Meal.diner_id == user_id, Meal.meal_avail_date == day)
    test = [r.id for r in row_day]
    if not test:
        return None
    else:
        meal_avail_date = [r.meal_avail_date for r in row_day]
        string_date = meal_avail_date[0]
        datelist = [string_date.strftime("%A, %B, %d")]
        merged_list = [r.meal_title for r in row_day] + [r.meal_description for r in row_day] + datelist
        return merged_list

def query_tp1(user_id: int):
    day = date_today() + datetime.timedelta(days=1)
    session = DbSession.factory()
    #TODO: Implement error handling for multiple results on same day if chef makes two meals available on same day
    row_day = session.query(Meal).filter(Meal.diner_id == user_id, Meal.meal_avail_date == day)
    test = [r.id for r in row_day]
    if not test:
        return None
    else:
        meal_avail_date = [r.meal_avail_date for r in row_day]
        string_date = meal_avail_date[0]
        datelist = [string_date.strftime("%A, %B, %d")]
        merged_list = [r.meal_title for r in row_day] + [r.meal_description for r in row_day] + datelist
        return merged_list

def query_tp2(user_id: int):
    day = date_today() + datetime.timedelta(days=2)
    session = DbSession.factory()
    #TODO: Implement error handling for multiple results on same day if chef makes two meals available on same day
    row_day = session.query(Meal).filter(Meal.diner_id == user_id, Meal.meal_avail_date == day)
    test = [r.id for r in row_day]
    if not test:
        return None
    else:
        meal_avail_date = [r.meal_avail_date for r in row_day]
        string_date = meal_avail_date[0]
        datelist = [string_date.strftime("%A, %B, %d")]
        merged_list = [r.meal_title for r in row_day] + [r.meal_description for r in row_day] + datelist
        return merged_list

def query_tp3(user_id: int):
    day = date_today() + datetime.timedelta(days=3)
    session = DbSession.factory()
    #TODO: Implement error handling for multiple results on same day if chef makes two meals available on same day
    row_day = session.query(Meal).filter(Meal.diner_id == user_id, Meal.meal_avail_date == day)
    test = [r.id for r in row_day]
    if not test:
        return None
    else:
        meal_avail_date = [r.meal_avail_date for r in row_day]
        string_date = meal_avail_date[0]
        datelist = [string_date.strftime("%A, %B, %d")]
        merged_list = [r.meal_title for r in row_day] + [r.meal_description for r in row_day] + datelist
        return merged_list

def query_tp4(user_id: int):
    day = date_today() + datetime.timedelta(days=4)
    session = DbSession.factory()
    #TODO: Implement error handling for multiple results on same day if chef makes two meals available on same day
    row_day = session.query(Meal).filter(Meal.diner_id == user_id, Meal.meal_avail_date == day)
    test = [r.id for r in row_day]
    if not test:
        return None
    else:
        meal_avail_date = [r.meal_avail_date for r in row_day]
        string_date = meal_avail_date[0]
        datelist = [string_date.strftime("%A, %B, %d")]
        merged_list = [r.meal_title for r in row_day] + [r.meal_description for r in row_day] + datelist
        return merged_list

def query_tp5(user_id: int):
    day = date_today() + datetime.timedelta(days=5)
    session = DbSession.factory()
    #TODO: Implement error handling for multiple results on same day if chef makes two meals available on same day
    row_day = session.query(Meal).filter(Meal.diner_id == user_id, Meal.meal_avail_date == day)
    test = [r.id for r in row_day]
    if not test:
        return None
    else:
        meal_avail_date = [r.meal_avail_date for r in row_day]
        string_date = meal_avail_date[0]
        datelist = [string_date.strftime("%A, %B, %d")]
        merged_list = [r.meal_title for r in row_day] + [r.meal_description for r in row_day] + datelist
        return merged_list

def query_tp6(user_id: int):
    day = date_today() + datetime.timedelta(days=6)
    session = DbSession.factory()
    #TODO: Implement error handling for multiple results on same day if chef makes two meals available on same day
    row_day = session.query(Meal).filter(Meal.diner_id == user_id, Meal.meal_avail_date == day)
    test = [r.id for r in row_day]
    if not test:
        return None
    else:
        meal_avail_date = [r.meal_avail_date for r in row_day]
        string_date = meal_avail_date[0]
        datelist = [string_date.strftime("%A, %B, %d")]
        merged_list = [r.meal_title for r in row_day] + [r.meal_description for r in row_day] + datelist
        return merged_list
