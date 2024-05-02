from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

import json
import urllib.parse

#My database for discussion
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newgoat.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Messidatapage(db.Model):
    teamName = db.Column(db.String(), primary_key = True)
    goalsScored = db.Column(db.Integer())
    assists = db.Column(db.Integer())
    titlesWon = db.Column(db.String())

    def __repr__(self):
        return f'<Messidatapage: {self.teamName}'

class Ronaldodatapage(db.Model):
    teamName = db.Column(db.String(), primary_key = True)
    goalsScored = db.Column(db.Integer())
    assists = db.Column(db.Integer())
    titlesWon = db.Column(db.String())

    def __repr__(self):
        return f'<Ronaldodatapage: {self.teamName}'

class User(db.Model):
    id = db.Column(db.Integer(), primary_key = True, autoincrement=True)
    user_name = db.Column(db.String())    

    def __repr__(self):
        return f'<User: {self.id}'

class Comments(db.Model):
    id = db.Column(db.Integer(), primary_key = True, autoincrement=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    comment = db.Column(db.Text())

    User = db.relationship('User', backref='comments')
    def __repr__(self):
        return f'<Comments: {self.id}'







@app.route("/commented", methods=['POST'])
def commented():

    # Decode URL-encoded string
    decoded_string = urllib.parse.unquote(request.data.decode())

    # Extract JSON part
    json_string = decoded_string.split('=', 1)[1]

    # Parse JSON string to JSON object
    json_object = json.loads(json_string)

    # Print JSON object
    print(json_object["username"])
    print(json_object["comment"])

    newUser = User(
    user_name=json_object['username']
    )
    db.session.add(newUser)
    db.session.commit()
    newComment = Comments(
        user_id=newUser.id,
        comment=json_object["comment"],
    )


    db.session.add(newComment)
    db.session.commit()

    return "Test"



#Routing the pages of the site
@app.route("/")
@app.route("/homepage")
def homepage():
    return render_template("homepage.html")
@app.route("/messi")
def messi():
    return render_template("messi.html")
@app.route("/ronaldo")
def ronaldo():
    return render_template("ronaldo.html")
@app.route("/comparison")
def  comparison():
    return render_template( "comparison.html" )
@app.route("/contact")
@app.route("/contactme")
def contact():
    return render_template("contact.html")
@app.route("/discussion")
@app.route("/discuss")
def discussion():
    return render_template('discussion.html', comments = Comments.query.all())


if __name__ == "__main__":
    # Change to False when deploying.
    app.run(debug=False)