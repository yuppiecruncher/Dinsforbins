from dins import DbSession
from typing import *
from dins.data.meals import Meal
from dins.data.users import User
import datetime


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
