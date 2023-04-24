# -*- coding: utf-8 -*-
from flask import Flask,render_template,request,redirect
# 创建程序
# web应用程序
app = Flask(__name__)

# @app.route('/',methods = ['POST','GET'])
# def index():
#    return render_template("test.html")


@app.route('/w1',methods = ['POST','GET'])
def login():
    username = request.form.get('username')
    password = request.form.get('pw')
    if username =='2528104776' and password=='123':
        return "登录成功!"
    else:
        return render_template('w1.html',msg = "登录失败！")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001,debug = True)
