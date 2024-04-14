from modules.app import app
from modules.db import engine, Session
from modules.models import DBase


@app.before_first_request
def create_tables():
    DBase.metadata.create_all(engine)

@app.teardown_appcontext
def clean(exception=None):
    Session.remove()
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)
