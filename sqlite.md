# SQLite Configuration

## Description
When we're doing our own development locally we don't want interfere with the actual database the website is using,
so instead this will set up a SQLite database you can alter all you want to run locally with some preset data.

## Setup Instructions
1. `cd` into the top directory of this project.
2. `python manage.py migrate` - To create the database and tables appropriately
3. `python manage.py loaddata undocuscholar/fixtures/initial_data.json`
