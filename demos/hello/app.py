"""
请将此文件夹和pipfile pipfile.lock复制到本地
然后进入文件目录：打开cmd
输入：
pip install pipenv
pipenv install
pipenv shell
flask run
现在使用浏览器打开“http://127.0.0.1:5000/hello/你的名字”即可体验
下次开启只需在文件目录cmd输入：
pipenv shell
flask run
若要部署上线，请搜索Pythonanywhere
更多资料请见《Flask Web开发实战 入门进阶和原理解析》
刘家朋 2020/4/1
"""
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
