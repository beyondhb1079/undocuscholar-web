import os, sys
import sqlite3
import json
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, Response
from flask.views import MethodView
from werkzeug import Headers

# Create the application
app = Flask(__name__)
app.config.from_object(__name__)
app.debug = True

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'backend.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('API_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    # TODO: Only init if the db doesn't exist yet
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print 'Initialized the database.'

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


# API section

@app.route('/')
def index():
    sys.stderr.write('running...') 
    return 'Test Page\n'

@app.route('/api')
def doc():
    return 'TODO: Document the API here\n'

class ScholarshipAPI(MethodView):
    # TODO: Backend needs to decide whether to use raw SQL or sqlalchemy for
    # reading/writing to the database
    def get(self, item_id):
        if item_id is None:
            # Use request.args.get(key, default) to get the filtering arguments
            response = {
              "code": 0,
              "message": "List of Scholarships",
              "results": [
                {
                  "name": "Frank F. Conlon Fellowship",
                  "deadline": "1/15/2016",
                  "amount": 8000
                },
                {
                  "name": "WAVA Phyllis Lawson Scholarship Award",
                  "deadline": "1/31/2016",
                  "amount": 1000
                }
              ]
            }
            response["filters"] = request.args
            headers = Headers()
            headers.add('Access-Control-Allow-Origin', '*')
            if "pretty" in request.args:
                return Response(json.dumps(response, indent=2), mimetype='application/json', headers=headers)
            return Response(json.dumps(response), mimetype='application/json', headers=headers)
        else:
            return 'TODO: Get scholarship with id: %d\n' % item_id

    def post(self, item_id):
        if item_id is None:
            # Use request.form[key] to get the mappings
            # You can use the wtforms library to validate input
            return 'TODO: Create scholarship using properties: \n\n%s\n' % \
                    json.dumps(request.form, indent=2)
        else:
            return 'TODO: Unarchive scholarship with id: %d\n' % item_id

    def put(self, item_id):
        # Use request.form[key] to get the mappings
        # You can use the wtforms library to validate input
        return 'TODO: Update scholarship with id %d using properties: \n\n%s\n' % \
                (item_id, json.dumps(request.form, indent=2))

    def delete(self, item_id):
        return 'TODO: Archive scholarship with id: %d\n' % item_id

scholarship_view = ScholarshipAPI.as_view('scholarship_api')
app.add_url_rule('/api/scholarships', defaults={'item_id': None},
                 view_func=scholarship_view, methods=['GET',])
app.add_url_rule('/api/scholarships', view_func=scholarship_view, methods=['POST',])
app.add_url_rule('/api/scholarships/<int:item_id>', view_func=scholarship_view,
                 methods=['GET', 'PUT', 'DELETE', 'POST'])

if __name__ == '__main__':
    sys.stderr.write('running...') 
    app.run()