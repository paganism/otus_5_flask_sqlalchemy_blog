# Simple blog on flask and SQLAlchemy
This app creates simple blog pages. DB-engine - sqlite3.

# How to run on Linux (python3.6 or higher). For localhost only.
* Download code
* Install requirements `$ pip install -r requirements.txt`
* Set up environment variables:
```
$ export FLASK_APP=blog.py
$ export FLASK_DEBUG=1 (only if you need debug mode)
$ export DATABASE_URL=... (prefered path to db)
$ export SECRET_KEY=YOUR_SECRET_KEY
```
Instead of this action you can hold your own .env file
* Run application `$ flask run`
* Go to page http://127.0.0.1:5000/

# Goals
This code is writtem for educational purposes only