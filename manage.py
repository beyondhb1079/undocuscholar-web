#!/usr/bin/env python3
from os import environ
from os.path import exists, getmtime

import sys
from subprocess import call
from shutil import which
from django.core.management import execute_from_command_line

def last_modified_time(path):
    return exists(path) and getmtime(path)

def setup():
    """Sets things up"""
    if sys.argv[1] != 'runserver':
        return

    if 'DATABASE_URL' not in environ and 'ENV' not in environ and not exists('db.sqlite3'):
        # Check Python version
        assert sys.version_info >= (3, 4), "Python 3.4+ required"

        # Do initial migration and mock data load
        print("Setting up local database...")
        execute_from_command_line([sys.argv[0], "migrate"])
        execute_from_command_line([sys.argv[0], "loaddata", "undocuscholar/fixtures/initial_data.json"])

    # Automatically downloads JS/CSS dependencies. It's hackish, but will do for now.
    if last_modified_time('package.json') > last_modified_time('node_modules'):
        # static/node_modules is nonexistent or out of date. Automatically
        print('Changes in package.json were detected. Downloading node packages to node_modules...')
        assert which("npm"), "npm needs to be installed: https://nodejs.org/en/download/"
        call([which("npm"), "install"])

if __name__ == "__main__":
    environ.setdefault("DJANGO_SETTINGS_MODULE", "undocuscholar.settings")
    setup()
    execute_from_command_line(sys.argv)


