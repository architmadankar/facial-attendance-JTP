from modules.models import DBase
from modules.app import app
from modules.db import engine, Session

def create_tables():
    DBase.metadata.create_all(engine)
    
@app.teardown_appcontext
def clean(exception=None):
    Session.remove()
    
if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0', threaded=True)