import os, sys
import json
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, Response
from flask.views import MethodView
from flask_sqlalchemy import SQLAlchemy
from werkzeug import Headers
import psycopg2
import urlparse

# Create the application
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

app.debug = True
app.config.from_envvar('API_SETTINGS', silent=True)

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
                  "amount": 8000,
                  "url": "http://southasia.washington.edu/students/funding/#Conlon"
                },
                {
                  "name": "WAVA Phyllis Lawson Scholarship Award",
                  "deadline": "1/31/2016",
                  "amount": 1000,
                  "url": "TBD"
                },
                {
                  "name": "Mount Baker Community Club MLK Scholarship",
                  "deadline": "1/15/2016",
                  "amount": 10000,
                  "url": "http://www.mountbaker.org/scholarship/"
                },
                {
                  "name": "Annual Arevalo Scholarship",
                  "deadline": "3/14/2016",
                  "amount": 1000,
                  "url": "http://www.ewu.edu/Documents/CSBSSW/Chicano%20Ed/Scholarships%202015-16/Arrevalo%20Scholarship%202015.pdf"
                },
                {
                  "name": "Orgullo Latino(a) University Scholarship",
                  "deadline": "3/14/2016",
                  "amount": 1000,
                  "url": "http://www.fastweb.com/college-scholarships/scholarships/19801-orgullo-latino-university-scholarship"
                },
                {
                  "name": "Bernie Minsk Scholarship",
                  "deadline": "3/1/2016",
                  "amount": 30000,
                  "url": "http://www.berniescholarships.org/Apply.html"
                },
                {
                  "name": "Walter H. Meyer - Garry L. White Memorial Scholarship",
                  "deadline": "3/1/2016",
                  "amount": 5000,
                  "url": "http://www.collegeplan.org/cpnow/pnwguide/onlineaps/mwonap.htm"
                },
                {
                  "name": "Yuri and Tatsuo Nakata Scholarship",
                  "deadline": "3/1/2016",
                  "amount": 2500,
                  "url": "http://www.washboard.org/ScholarshipDetails/The+Seattle+Foundation/2016-2017/Yuri+and+Tatsuo+Nakata+Scholarship"
                }
              ]
            }
            response["request_params"] = request.args
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