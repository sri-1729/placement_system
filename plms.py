from app import create_app, db
from app.models import Login


app = create_app('development')


@app.shell_context_processor
def make_shell_context():
	return dict(db=db, Login=Login)