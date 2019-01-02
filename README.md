# Dinsforbins

--IN PROGRESS--

Simple Dinner Reservation Web Application Based on Python3

The goal of this project is to deploy a live web application with some key features.

This web application will allow a user (diner) to reserve menu options and times from a list populated by a content producer (the chef). A third user type (the analyst) will be able to see usage statistics, survey responses and other relevant data through a built-in dashboard.

The webapp is built upon the following stack:

Pyramid Framework (https://trypyramid.com/)
<p>  -utilizing Chameleon template
<p>Twitter Bootstrap (https://getbootstrap.com/2.0.4/)
<p>SQLAlchemy (and Alembic) (https://www.sqlalchemy.org/)
<p>Postgresql (https://www.postgresql.org/)
<p>Twilio (https://www.twilio.com/)

Planned functionality:
-Account management and role assignment (diner, chef, analyst)
-Basic HTML error correction
-Cookie sessions
-Email confirmation, notifications and surveys

To run this website on your local machine, you will need virtualenv(https://virtualenv.pypa.io/en/latest/). clone the repository to your machine. Using your command-line interface navigate to the folder 'dins' containing the development.ini file. Activate the virtual environment (on linux/mac it should be 'source venv/bin/activate') and run pserve development.ini . You can now open any browser and type 'localhost' to view the site.

You may wish to update pip and setuptools, depending on how out of date the versions included in the repository are. On mac/linux command line this is pip install -U pip setuptools.

Personal note: this app is being created for my partner. Its namesake comes from their nickname - Bins. Hence "Dinner for Partner" or "Dinsforbins")
