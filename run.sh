# TODO: Detect if being sourced, if not, notify the user
export FLASK_APP=backend_app.py
export FLASK_DEBUG=1
# In production: flask run --host=0.0.0.0
flask run
