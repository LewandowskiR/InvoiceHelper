# -*- coding: utf-8 -*-
from website import create_app, db
from website.models import User, Invoice


app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Invoice': Invoice}

if __name__ == '__main__':
    app.run(debug=True)