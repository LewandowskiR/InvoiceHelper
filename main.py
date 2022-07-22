# -*- coding: utf-8 -*-
from website import create_app, db
from website.models import User


app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}

if __name__ == '__main__':
    app.run(debug=True)