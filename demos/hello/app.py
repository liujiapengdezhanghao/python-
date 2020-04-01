from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import random


app = Flask(__name__)


bs = Bootstrap(app)
app.config["BOOTSTRAP_SERVE_LOCAL"] = True


@app.route("/hello/<name>")
def hello(name="flask"):
   return render_template('hello.html', name=name,bs=bs) 
   
   
@app.route("/get/havepaihao")
def paihao():
   u = random.randint(1000000000,9999999999)
   return "<h2>你的唯一饲养牌号是:%d</h2>" % u
              
