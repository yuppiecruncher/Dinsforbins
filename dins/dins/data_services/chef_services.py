from dins import DbSession
from typing import *
from dins.data.meals import Meal
from dins.data.users import User
from dins.data.linked_users import Link
from sqlalchemy.util import KeyedTuple
import datetime
from dins.data_services import user_services
from sqlalchemy import and_

####################### QUERY DINERS FOR DISPLAY ####################################################

def query_assigned_diner(user_id: int):
    session = DbSession.factory()
    rows = session.query(Link).filter(Link.chef_id == user_id)
    if not rows:
        return None
    diner_ids = [d.diner_id for d in rows]
    diner_rows = session.query(User).filter(User.id.in_(diner_ids))

    return diner_rows

####################### ASSIGN DINERS TO CHEF ####################################################

def assigned_diner(user_id: int, diner_email: str):
    session = DbSession.factory()
    ##### check if user exists #####
    submitted_email = diner_email.lower().strip()
    user = session.query(User).filter(User.email == submitted_email).first()

    if not user:
        return None

    #### insert into linked table ###
    link = Link()
    link.chef_id = user_id
    link.diner_id = user.id
    session.add(link)
    session.commit()
    return link

####################### ADD MEALS TO DB ####################################################

def create_meal(title: str, menudescription: str, available: str, user_id: int, diner_email: str) -> Meal:
    session = DbSession.factory()
    meal = Meal()
    meal.meal_title = title
    meal.meal_description = menudescription
    date_input = available
    year, month, day = map(int, date_input.split('-'))
    date1 = datetime.date(year, month, day)
    meal.meal_avail_date = date1
    meal.chef_id = user_id

    #### diner_email to diner_id conversion ####
    email = diner_email.lower().strip()
    user = session.query(User).filter(User.email == email).first()
    if not user:
        return None
    diner_id = user.id
    ########                  ############

    meal.diner_id = diner_id
    session.add(meal)
    session.commit()

    return meal

def diner_validation(diner_email: str):
        session = DbSession.factory()
        email = diner_email.lower().strip()
        user = session.query(User).filter(User.email == email).first()
        if not user:
            return None

        return user

################## QUERY FOR WEEKLY MEALS BY DAY #####################################################
def date_today():
    today = datetime.datetime.now()
    today = today.replace(hour=0, minute=0, second=0, microsecond=0)
    return today

def query_today(user_id: int):
    day = date_today()
    session = DbSession.factory()
    #TODO: Implement error handling for multiple results on same day if chef makes two meals available on same day
    row_day = session.query(Meal).filter(Meal.chef_id == user_id, Meal.meal_avail_date == day)
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
    row_day = session.query(Meal).filter(Meal.chef_id == user_id, Meal.meal_avail_date == day)
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
    row_day = session.query(Meal).filter(Meal.chef_id == user_id, Meal.meal_avail_date == day)
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
    row_day = session.query(Meal).filter(Meal.chef_id == user_id, Meal.meal_avail_date == day)
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
    row_day = session.query(Meal).filter(Meal.chef_id == user_id, Meal.meal_avail_date == day)
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
    row_day = session.query(Meal).filter(Meal.chef_id == user_id, Meal.meal_avail_date == day)
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
    row_day = session.query(Meal).filter(Meal.chef_id == user_id, Meal.meal_avail_date == day)
    test = [r.id for r in row_day]
    if not test:
        return None
    else:
        meal_avail_date = [r.meal_avail_date for r in row_day]
        string_date = meal_avail_date[0]
        datelist = [string_date.strftime("%A, %B, %d")]
        merged_list = [r.meal_title for r in row_day] + [r.meal_description for r in row_day] + datelist
        return merged_list
