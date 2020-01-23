from blog_engine import db


tags_posts_table = db.Table('tags_posts', db.Model.metadata,
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')),
)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)

    posts = db.relationship("Post", back_populates="user")

    def __repr__(self):
        return f'id: {self.id}, name: {self.username}'


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    posts = db.relationship("Post", secondary=tags_posts_table, back_populates="tags")

    def __repr__(self):
        return f'id: {self.id}, name: {self.name}' 


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(16))
    text = db.Column(db.Text)
    is_publised = db.Column(db.Boolean)
    user = db.relationship("User", back_populates="posts", lazy='joined')
    tags = db.relationship("Tag", secondary=tags_posts_table, back_populates="posts")

    def __repr__(self):
        return f'id: {self.id}, name: {self.title}'
