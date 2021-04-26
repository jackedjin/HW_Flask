from flask import render_template, redirect

from app import db
from app import app
from app.forms import MessageForm
from app.models import User, Messages

# add route '/' and also add the two methods to handle request: 'GET' and 'POST'
@myapp_obj.route("/", methods=['GET','POST'])

def home():
    form=MessageForm()
    if form.validate_on_submit():
        # check if user exists in database
        user = User.query.filter_by(author=form.author.data).first()
        if user is None
        
        # if not create user and add to database
        username = User(author = form.author.data)
        db.session.add(username)
            
        # create row in Message table with user (created/found) add to ta database
        database = Messages(message = form.message.data, user_id = User.query.filter_by(uername).first().id)
            db.session.add(database)
            db.session.commit()

    posts = [
        {   'author' : 'Carlos',
            'message' : 'Yo! Where you at?!'
        },
        {   'author' : 'Jerry',
            'message' : 'Home. You?'
        }
    ]

    dict_list = Message.query.all()
    for p in dict_list:
        posts = posts + [
        {
            f 'author: (User.query.filter_by(id = p.user_id).first())'
            f 'message: (p.message)'
        }]

    return render_template('home.html', posts=posts, form=form)

