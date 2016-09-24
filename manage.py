#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    first_time_sql_setup = 'DATABASE_URL' not in os.environ and 'ENV' not in os.environ and not os.path.exists('db.sqlite3')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "undocuscholar.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
    
    if first_time_sql_setup:
        print("First Time SQLite setup: TRUE")
        print("Please follow the instructions in sqlite.md or click this link: https://github.com/beyondhb1079/www/blob/master/sqlite.md")
