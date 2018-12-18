from flask import *

from .models import User, db

Root = Blueprint("root", __name__, template_folder="templates")

def authenticate(username, password):
  try:
    user = User.query.filter_by(username=username).first()

    if not user:
      return False

    return user.password == password
  except: #TODO: log error
    return False

@Root.route("/")
def index():
  return render_template("index.html", posts=[])

@Root.route("/register", methods=["GET", "POST"])
def register():
  from .forms import Register
  
  form = Register(request.form)
  
  if request.method == "POST" and form.validate():
    pass#newUser = User(email
  
  return render_template("register.html", form=form)

@Root.route("/login", methods=["GET", "POST"])
def login():
  from .forms import Login
  
  form = Login(request.form)
  
  if request.method == "GET" or not form.validate():
    return render_template("login.html", form=form)
  
  if not authenticate(form.email, form.password):
    flash("Invalid email/password combination", "error")
    
    return render_template("login.html", form=form), 401
  
  session["user"] = {"name": form.email}
  
  return redirect(url_for(".index"))

@Root.route("/logout")
def logout():
  if "user" not in session:
    abort(400)
  
  del session["user"]
  
  return redirect(url_for(".index"))

@Root.route("/post", methods=["GET", "POST"])
def post():
  if request.method == "GET":
    return render_template("post.html")