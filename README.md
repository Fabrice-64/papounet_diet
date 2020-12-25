# Overall Framework
This project is developped in the framework of an education program as software developper in Python.

# Purpose
This web application offers the user to look for food items with better nutritional properties.

# Main Functionalities
- The user can create an account in order to get a better experience
- The user, be he anonymous or registered, is supposed to type in the name of a food item
- Then, the application looks for items of the same category with better nutritional properties
- The user can get more information on a selected product
- And he can subsequently record it

# Environment
This project is developped using Python 3.8.1 and Django 3.1.2

# How to start the local server
- Create a virtual environment with python
- Install all the requirements, as depicted in the requirements.txt
- Install the modules
- switch to papounet_diet module
- run from the terminal: $ python manage.py runserver

# Testing:
## Scripts for efficient testing
Using the Shell, type what the following command line, it will remove almost all irrelevant files.
As of 23.12.20, coverage rate reaches 84%

$ coverage run --omit='*/venv/*,*/tests/*,*/migrations/*,*/papounet_diet/tests.py,*/papounet_diet/settings.py,*/manage.py,*/apps.py,*/admin.py'  manage.py test

$ coverage report -m

## Where the tests are located ?
App customer: only basic testing as this module strictly follows Django guidelines.
App food_items:
- in module openfoodfacts, iot check the import of data through their API
- in app food_items, iot check the views and the queries.
- in papounet_diet, you will find the Selenium functional tests, with two user stories.

# Architecture
Only the folders are depicted.
This program follows a Django standard architecture.

|- papounet_diet
    |-  customer
    |           |-  templates
    |           |            |-  customer
    |           |-  tests
    |
    |-  food_items
    |           |-  fixtures
    |           |-  management
    |           |           |-  commands
    |           |-  openfoodfacts
    |           |           |- tests
    |           |           |       |-  off_data_to_be_tested
    |           |-  templates
    |           |           |-  food_items
    |           |-  tests
    |-  papounet_diet
    |           |- static



