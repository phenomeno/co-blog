from app import app
from flask import render_template
from flask import request
from app import models
from flask import session
from flask import redirect
from flask import url_for
from app import db
from flask import flash

@app.route('/')
@app.route('/index')
def index():
    page = int(request.args.get('page', 1))

    max_page_no = models.Post.query.count()
    if max_page_no % 3 == 0:
        max_page_no = max_page_no / 3
    else:
        max_page_no = (max_page_no / 3) + 1

    posts = models.Post.query.order_by('created_time desc') \
        .offset((page-1)*3) \
        .limit(3) \
        .all()
    return render_template('index.html', title='welcome', posts=posts, page=page, max_page_no=max_page_no)

@app.route('/login')
def login():
    return render_template('login.html', title='login')

@app.route('/login_ok', methods=['POST'])
def login_ok():
    form_nick = request.form['nickname']
    form_pass = request.form['password']
    model_user = models.User.query.filter_by(nickname=form_nick).first()
    if model_user:
        if form_pass == model_user.password:
            session['user_id'] = model_user.id
            return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

@app.route('/post')
def post():
    if 'user_id' in session:
        return render_template('post.html', title='post')
    return redirect(url_for('login'))

@app.route('/post_ok', methods=['POST'])
def post_ok():
    if 'user_id' in session:
        user_id = int(session['user_id'])
        form_title = request.form['title']
        form_post = request.form['post']
        model_user = models.User.query.get(user_id)
        try:
            # add and commit post to model
            p = models.Post()
            p.user_id = user_id
            p.title = form_title
            p.body = form_post
            db.session.add(p)
            db.session.commit()
        except:
            return redirect(url_for('post'))
        return redirect(url_for('index'))
    return redirect(url_for('login'))


@app.route('/post/<post_id>')
def view_post(post_id):
    post = models.Post.query.get(int(post_id))
    return render_template('post_view.html', post=post)

@app.route('/comment_ok', methods=['POST'])
def comment_ok():
    form_post_id = request.form['post_id']
    form_nick = request.form['nickname']
    form_email = request.form['email']
    form_comment = request.form['comment']
    try:
        c = models.Comment()
        c.post_id = int(form_post_id)
        c.nickname = form_nick
        c.email = form_email
        c.body = form_comment
        db.session.add(c)
        db.session.commit()
    except:
        flash("Comment wasn't saved. Try again?")
        return redirect(url_for('view_post', post_id = form_post_id))
    return redirect(url_for('view_post', post_id = form_post_id))

@app.route('/logout')
def logout():
    if 'user_id' in session:
        session.pop('user_id')
    return redirect(url_for('index'))
