# Customer Support Ticketing System
### A web application built using Django with a simple UI demonstrating the use of views, templates and models for data storage and retrieval.

## Description-
This lightweight app uses only django and python-dotenv as it's dependencies. It has views for user authentication and registration
that make use of Form fields provided by Django. It has built in client-side checks for different fields. They can be customized
as per your need. The UI is deliberately kept as minimal as possible so that you can add your own styling and maybe even expand the 
number of views to include a third view for staff members, apart from the two that are present (user and superuser).

The user posts a ticket/complaint, the superuser/admin posts a response while automatically marking the ticket as resolved. The resolved
ticket then gets moved to the Responded Tickets section in the user's dashboard.

You can add more form fields in the login, register and dashboard views and templates. Also be sure to update the models accordingly to create the
tables correctly. I did not have any use for the email field so I excluded it.

## Dependencies
### 1. django (4.1.6)
### 2. python-dotenv

# Build Commands
### Creating a venv is optional but recommended. Use the standard way to create and activate a virtual environment.
### pip install django python-dotenv
### python manage.py makemigrations
### python manage.py migrate
Verify whether migrations for ticketing_app_usersubmitteddata and ticketing_app_respondeddata have been completed
### python manage.py createsuperuser
provide the username, email and password you want to set as the admin/superuser of the website. You can later sign in to the app's admin view 
with the username and password you provided and you can respond to the tickets submitted.
### Change the .env.example file to .env file

# Hosting
### For hosting, the platform I used was pythonanywhere.com where you can clone your git repository, set the wsgi configuration file in the
### 'Web' section of the user dashboard. The only problem is that they do not have the latest version of python built-in. Create your virtual
### using the bash console's mkvirtualenv my-virtual-env method. It automatically activates your environment and you only have to install
### dependencies like django and python-dotenv using pip after which the standard build commands will usually work. Sometimes the tables
### might not be created as expected but you can run 
## python manage.py makemigrations ticketing_app 
### followed by running the normal migrate command to explicitly specify where the required models.py file is located. Then the standard .env
## file needs to be created and you're good to go.
