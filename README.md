# Dinsforbins

--IN PROGRESS--

Simple Dinner Reservation Web Application Based on Python3

The goal of this project is to deploy a live web application with some key features.

This web application will allow a user (diner) to reserve menu options and times from a list populated by a content producer- (the chef). A third user type (the analyst) will be able to see usage statistics, survey responses and other relevant data through a built-in dashboard.

The webapp is built upon the following stack:

Pyramid Framework (https://trypyramid.com/)
<p>  Cookiecutter for pyramid-starter (https://github.com/Pylons/pyramid-cookiecutter-starter)
<p>   -utilizing Chameleon template
<p>Twitter Bootstrap (https://getbootstrap.com/2.0.4/)
<p>SQLAlchemy (and Alembic) (https://www.sqlalchemy.org/)
<p>Postgresql (https://www.postgresql.org/)
<p>Passlib (https://bitbucket.org/ecollins/passlib/wiki/Home)
<p>Twilio (https://www.twilio.com/)


Planned functionality:
-Account management and role assignment (diner, chef, analyst)
-Data-driven interactions between diner and chef and interactive SQLAlchemy-based queries for the Analyst.
-Basic HTML form-based error correction of input data (with proper escaping and security protocols to prevent attacks.)
-Cookie sessions
-Email based confirmation, notifications and surveys
-DB migration and modification with Alembic to allow for migration to postgresql or noSQL based DB such as MongoDb.

To run this website on your local machine, you will need virtualenv(https://virtualenv.pypa.io/en/latest/). clone the repository to your machine. Using your command-line interface navigate to the folder 'dins' containing the development.ini file. Activate the virtual environment (on linux/mac it should be 'source venv/bin/activate') and run pserve development.ini . You can now open any browser and type 'localhost' to view the site.

The first time this stack is run, install the dependencies by running "$ setup.py develop" in the virtual environment

You may wish to update pip and setuptools, depending on how out of date the versions included in the repository are. On mac/linux command line this is pip install -U pip setuptools.

Personal note: this app is being created for my partner. Its namesake comes from their nickname - Bins. Hence "Dinner for Partner" or "Dinsforbins")
