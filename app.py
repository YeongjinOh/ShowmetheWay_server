from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User

engine = create_engine('sqlite:///user.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/scores/')
def showAll():
    users = session.query(User).all()
    output = "<h1>Score lists</h1>"
    output += "</br>"
    for user in users:
        output += "%s" % user.id
        output += "</br>"
        output += "name : %s" % user.name
        output += "</br>"
        output += "score : %s" % user.score
        output += "</br></br>"
    return output

@app.route('/scores/new/', methods=['GET','POST'])
def newUser():
    if request.method == 'POST':
        user = User(name=request.form['name'], email=request.form['email'], score=int(request.form['score']))
        session.add(user)
        session.commit()
        return redirect(url_for('showAll'))
    else:
        return render_template('newUser.html')
    return "page to add user"
if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)

