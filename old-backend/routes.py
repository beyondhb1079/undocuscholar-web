import json
from base_app import app, db
from flask.views import MethodView
from flask import request, Response
from models import Scholarship
from werkzeug import Headers

@app.route('/')
def index():
    sys.stderr.write('running...') 
    return 'Test Page\n'

@app.route('/api')
def doc():
    return 'TODO: Document the API here\n'

def create_response(code=0, message="Success", pretty=False, **kwargs):
    """Creates a Response object appropriated with the given arguments"""
    kwargs['code'] = code
    kwargs['message'] = message
    kwargs['request_params'] = request.args
    headers = Headers()
    headers.add('Access-Control-Allow-Origin', '*')
    if pretty:
        return Response(json.dumps(kwargs, indent=2), mimetype='application/json', headers=headers)
    else:
        return Response(json.dumps(kwargs), mimetype='application/json', headers=headers)

class ScholarshipAPI(MethodView):
    # TODO: Backend needs to decide whether to use raw SQL or sqlalchemy for
    # reading/writing to the database
    def get(self, item_id):
        if item_id is None:
            # Use request.args.get(key, default) to get the filtering arguments
            # scholarships = [
            #     {
            #       "name": "Frank F. Conlon Fellowship",
            #       "deadline": "1/15/2016",
            #       "amount": 8000,
            #       "url": "http://southasia.washington.edu/students/funding/#Conlon"
            #     },
            #     {
            #       "name": "WAVA Phyllis Lawson Scholarship Award",
            #       "deadline": "1/31/2016",
            #       "amount": 1000,
            #       "url": "TBD"
            #     },
            #     {
            #       "name": "Mount Baker Community Club MLK Scholarship",
            #       "deadline": "1/15/2016",
            #       "amount": 10000,
            #       "url": "http://www.mountbaker.org/scholarship/"
            #     },
            #     {
            #       "name": "Annual Arevalo Scholarship",
            #       "deadline": "3/14/2016",
            #       "amount": 1000,
            #       "url": "http://www.ewu.edu/Documents/CSBSSW/Chicano%20Ed/Scholarships%202015-16/Arrevalo%20Scholarship%202015.pdf"
            #     },
            #     {
            #       "name": "Orgullo Latino(a) University Scholarship",
            #       "deadline": "3/14/2016",
            #       "amount": 1000,
            #       "url": "http://www.fastweb.com/college-scholarships/scholarships/19801-orgullo-latino-university-scholarship"
            #     },
            #     {
            #       "name": "Bernie Minsk Scholarship",
            #       "deadline": "3/1/2016",
            #       "amount": 30000,
            #       "url": "http://www.berniescholarships.org/Apply.html"
            #     },
            #     {
            #       "name": "Walter H. Meyer - Garry L. White Memorial Scholarship",
            #       "deadline": "3/1/2016",
            #       "amount": 5000,
            #       "url": "http://www.collegeplan.org/cpnow/pnwguide/onlineaps/mwonap.htm"
            #     },
            #     {
            #       "name": "Yuri and Tatsuo Nakata Scholarship",
            #       "deadline": "3/1/2016",
            #       "amount": 2500,
            #       "url": "http://www.washboard.org/ScholarshipDetails/The+Seattle+Foundation/2016-2017/Yuri+and+Tatsuo+Nakata+Scholarship"
            #     }
            #   ]
            scholarships = map(lambda s: s.short_dict(), Scholarship.query.all())
            response = {
              'scholarships': scholarships,
              'page_info': {
                'page_size': len(scholarships),
                'page_num': 0,
                'more_pages': False
              }
            }
            headers = Headers()
            headers.add('Access-Control-Allow-Origin', '*')
            return create_response(pretty=('pretty' in request.args), **response)
        else:
            # TODO: Be more robust handling invalid id
            scholarship = db.session.query(Scholarship).filter_by(id = item_id)[0].full_dict()
            return create_response(scholarship=scholarship)

    def post(self, item_id):
        if item_id is None:
            # Use request.form[key] to get the mappings
            # You can use the wtforms library to validate input
            # TODO: Be robust about arguments as well.
            scholarship = Scholarship(**request.form)
            db.session.add(scholarship)
            db.session.commit()
            response = {
                'scholarship_id': scholarship.id
            }
            
            return create_response(message="Scholarship Created", pretty="pretty" in request.args, **response)
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