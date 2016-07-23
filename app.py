from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Rank

engine = create_engine('sqlite:///rank.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/score/')
def showAll():
    ranks = session.query(Rank).all()
    output = "<h1>Score lists</h1>"
    output += "</br>"
    for i in ranks:
        output += "%d" % i.id
        output += "</br>"
        output += "name : %s" % i.name
        output += "</br>"
        output += "score : %d" % i.score
        output += "</br></br>"
    return output

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)

