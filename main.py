from flask import Flask, render_template
from flask_restful import reqparse, abort, Api, Resource
from data import db_session

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = "Hello"


@app.route('/')
def index():
    return render_template('index.html')


def main():
    db_session.global_init("db/formulas.db")
    app.run()


if __name__ == '__main__':
    main()
