from flask import Flask, render_template, current_app, url_for
from blog_engine import app
from blog_engine.models import Post
from flask import request


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/posts')
def posts():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.id.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('posts', page=posts.next_num) if posts.has_next else None
    prev_url = url_for('posts', page=posts.prev_num) if posts.has_prev else None

    return render_template('posts.html', posts=posts.items,
                                            next_url=next_url,
                                            prev_url=prev_url)


@app.route('/<int:id>/', endpoint='post')
def post(id):
    
    curr_post = Post.query.filter(Post.id==id).scalar()

    return render_template('post.html', curr_post=curr_post, name=id)
