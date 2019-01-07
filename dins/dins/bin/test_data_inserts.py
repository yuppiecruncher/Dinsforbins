import os
import dins
import datetime
from dins import DbSession
from dins.data.meals import Meal
from dins.data.users import User

def main():
    init_db()
    while True:
        insert_some_data()

def insert_some_data():
    m = Meal()
    m.id = input("Meal ID: ")
    m.meal_title = input("Meal title: ")
    m.meal_description = input("Meal description: ")
    date_input = input("Meal available dates ('YYYY-MM-DD format'): ")
    year, month, day = map(int, date_input.split('-'))
    date1 = datetime.date(year, month, day)
    m.meal_avail_date = date1
    m.f_name = input("Users first name: ")
    m.l_name = input("Users last name: ")
    m.email = input("Users email address: ")
    m.hashed_password = input("Users password: ")
    m.role = input("Users role (Chef, Diner, Analyst): ")

    session = DbSession.factory()

    session.add(m)

    session.commit()

def init_db():
    top_folder = os.path.dirname(dins.__file__)
    rel_file = os.path.join('db','dins.sqlite')
    db_file = os.path.join(top_folder, rel_file)
    DbSession.global_init(db_file)

if __name__ == '__main__':
    main()
