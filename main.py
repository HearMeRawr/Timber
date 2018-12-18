import os
import sys

from flask import Flask

from timber.views import Root
from timber.models import db

app = None

def make_app():
  app = Flask(__name__)
  app.config["SECRET_KEY"] = os.environ["SECRET"]
  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
  
  db.init_app(app)
  app.register_blueprint(Root)
  
  return app

if __name__ == "__main__":
  app = make_app()
