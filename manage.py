#!/usr/bin/env python
import os
import sys
from subprocess import call
from shutil import which

if __name__ == "__main__":
    first_time_sql_setup = 'DATABASE_URL' not in os.environ and 'ENV' not in os.environ and not os.path.exists('db.sqlite3')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "undocuscholar.settings")

    from django.core.management import execute_from_command_line

    # Hackish, but will do for now.
    call([which("npm"), "install", "--prefix", "static/", "static/"])

    execute_from_command_line(sys.argv)

    if first_time_sql_setup:
        print("First Time SQLite setup: TRUE")
        with open("sqlite.md") as f:
            for l in f:
                print(l)


