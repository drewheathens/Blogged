from flask import render_template,request,flash,redirect,url_for
from . import main
from flask_login import login_required,current_user
from app.models import User,Article,Comment
from datetime import datetime
from app import *
from .forms import *

@main.route('/')
#login required
def index():
   
    return render_template('index.html')

@main.route('/', methods=['GET','POST'])
def home():
    form = posts()
    if form.validate_on_submit():
        post = article(body=form.post.data, author = current_user, category = form.category.data)
        db.session.add(post)
        db.session.commit()
        flash('posted live!')
        return redirect(url_for('main.index'))
        
    posts = Article.retrieve_posts(id).all()
    return render_template("posts.html", title="home page", form = form, posts = posts)


@main.route('/posts',methods=['GET', 'POST'])
@login_required
def post():
   form = Post()
   if form.validate_on_submit():
       post = form.post.data
       category = form.category.data
       user = current_user


       new_Article = Article(body = post,category = category,user = user)

       # save article
       db.session.add(new_article)
       db.session.commit()

       return redirect(url_for('main.explore',uname = user.username))

   return render_template('posts.html',form = form)

@main.route('/user/<username>')
@login_required

def user_profile(username):

    user = User.query.filter_by(username=username).first_or_404()
    posts= [
    {
    'author':user, 'body':'test Posts#1'
    }

    ]
    return render_template('profile/user_profile.html',posts=posts, user=user)


# @main.route('/comments',methods=['GET'],['POST'])

# @main.route('/post/new', methods=['GET,[POST'])
# def new_post()
#     form = posts()
#     if form.validate_on_submit():
#        posted = form.content.data
#        new_post = Article(posted=posted, category=form.category.data, user=current_user)
#        new_post=save_Article()
#        return redirect(url_for('main.view_post'))
#     return render_template('posts.html', form=form)

# @main.route('article/new/view')
# def view_post():
#     post = Article.query.filter_by(category='Article')




