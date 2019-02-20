from flask import render_template,request,flash,redirect,url_for
from . import main
from flask_login import login_required,current_user
from app.models import User,Blog,Comments
from datetime import datetime
from app import db, photos
from .forms import PostForm,CommentForm
from ..requests import get_quotes


@main.route('/quotes', methods=['GET','POST'])
def quotes():
    quotes = get_quotes()
    print (quotes)

    return render_template('quotes.html',quotes = quotes)


@main.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@main.route('/')
# @login_required
def index():


    tech = Blog.query.filter_by(category='Technology').all()

    return render_template('index.html', tech=tech)




@main.route('/index', methods=['GET', 'POST'])
def home():
    form = PostForm()
    if form.validate_on_submit():
        post = Pitch(body=form.post.data, author=current_user, category=form.category.data)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('main.index'))

    posts = Blog.retrieve_posts(id).all()

    return render_template("posts.html", title='Home Page', form=form,posts=posts)

@main.route('/post', methods = ['GET','POST'])
@login_required
def post():
   form = PostForm()
   if form.validate_on_submit():
       post = form.post.data
       category = form.category.data
       user = current_user


       new_pitch = Pitch(body = post,category = category,user = user)

       # save pitch
       db.session.add(new_blog)
       db.session.commit()

       return redirect(url_for('main.explore',uname = user.username))

   return render_template('post.html',form = form)


@main.route('/post/<int:id>', methods = ['GET','POST'])
@login_required
def user_post(id):

    users_post = Blog.query.filter_by(user_id=id).all()
    return render_template('user_posts.html',users_post = users_post)

@main.route('/technology' ,methods = ['GET','POST'])
def technology():
    technology = Blog.query.filter_by(category = 'Technology').all()
    form = CommentForm()
    if form.validate_on_submit():
        details = form.details.data
        user = current_user

        new_comment = Comments(details = details,blogs_id=id,user =user)
        # # save comment
        db.session.add(new_comment)
        db.session.commit()

    return render_template('technology.html', technology = technology,form=form)

@main.route('/sales' ,methods = ['GET','POST'])
def technolog():
    sales = Blog.query.filter_by(category = 'sales').all()
    form = CommentForm()
    if form.validate_on_submit():
        details = form.details.data
        user = current_user

        new_comment = Comments(details = details,blogs_id=id,user =user)
        # # save comment
        db.session.add(new_comment)
        db.session.commit()

    return render_template('sales.html', technology = technology,form=form)


    
@main.route('/explore')
@login_required
def explore():
    posts = Blog.query.order_by(Pitch.timestamp.desc()).all()
    return render_template('posts.html', title='Explore', posts=posts)


@main.route('/comments/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    comment = Comments.query.filter_by(blogs_id=id).all()

    form_comment = CommentForm()
    if form_comment.validate_on_submit():
        details = form_comment.details.data

        new_comment = Comments(details = details,blogs_id=id,user=current_user)
        # # save comment
        db.session.add(new_comment)
        db.session.commit()

    return render_template('comments.html',form_comment = form_comment,comment=comment)
@main.route('/user/<username>/update/pic',methods= ['POST'])
@login_required
def update_pic(username):
    user = User.query.filter_by(username = username).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('auth.user_profile',username=username))    


@main.route('/user/<username>')
@login_required
def user_profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {
            'author':user, 'body':'test Post#1'
        }
    ]
    return render_template('profile/user_profile.html',posts=posts, user=user)
    '''
    i have used a variant of first() called fist_or_404()
    which works exactly like first() when there are results, and in case there 
    are no results it auto sends a 404 error back
    '''




