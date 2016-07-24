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

@app.route('/scores/<int:user_id>/edit/', methods=['GET','POST'])
def editUser(user_id):
    user = session.query(User).filter_by(id = user_id).one()
    if request.method == 'POST':
        if request.form['name']:
            user.name = request.form['name']
        if request.form['email']:
            user.email = request.form['email']
        if request.form['score']:
            user.score = request.form['score']
        session.add(user)
        session.commit()
        return redirect(url_for('userJSON'))
    else:
        return render_template('editUser.html',user = user)

@app.route('/scores/insert/', methods=['GET','POST'])
def insertUser():
    if request.method == 'POST':
        key = request.form['email']
        userList = session.query(User).filter_by(email = key).all()
        if userList != [] :
            user = userList[0]
            user.name = request.form['name']
            user.score = request.form['score']
        else :
            user = User(name=request.form['name'], email=request.form['email'], score=int(request.form['score']))
        session.add(user)
        session.commit()
        users = session.query(User).all()
        return jsonify(User=[user.serialize for user in users])
    else :
        return render_template('insertUser.html')

@app.route('/scores/JSON')
def userJSON():
    users = session.query(User).all()
    return jsonify(User=[user.serialize for user in users])

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)

