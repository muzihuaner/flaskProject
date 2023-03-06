from flask import Flask, render_template, request
import pandas as pd
import time
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/register', methods=['GET','POST'])
def register():  # put application's code here
    if request.method == 'GET':
        return render_template("register.html")
    else:
        # return "注册成功！"
        # 1。接收用户Post提交的数据
        #     print(request.form)
        user = request.form.get('user')
        password = request.form.get('password')
        email = request.form.get('email')
        sex = request.form.get('sex')
        hobby = request.form.get('hobby')
        postion = request.form.get('postion')
        other = request.form.get('other')

        # 将文字写入表格
        df = pd.DataFrame(columns=['用户名', '密码', '电子邮箱', '性别', '爱好', '位置', '其他'])
        df.loc[len(df)] = [user, password, email, sex, hobby, postion, other]
        timestamp = int(time.time())
        filename = '用户表_{}.csv'.format(timestamp)
        df.to_csv(filename, index=False)
        return "注册成功！"


# @app.route('/get-reg',methods=['GET'])
# def get_register():
#     # return "注册成功！"
# # 1。接收用户Get提交的数据
#     print(request.args)
#     return "注册成功！"
#
# @app.route('/post-reg',methods=['POST'])
# def post_register():
#     # return "注册成功！"
# # 1。接收用户Post提交的数据
# #     print(request.form)
#     user=request.form.get('user')
#     password=request.form.get('password')
#     email=request.form.get('email')
#     sex=request.form.get('sex')
#     hobby=request.form.get('hobby')
#     postion=request.form.get('postion')
#     other=request.form.get('other')
#
#     # 将文字写入表格
#     df = pd.DataFrame(columns=['用户名','密码', '电子邮箱','性别','爱好','位置','其他'])
#     df.loc[len(df)] = [user,password,email,sex,hobby,postion,other]
#     timestamp = int(time.time())
#     filename = '用户表_{}.csv'.format(timestamp)
#     df.to_csv(filename, index=False)
#     return "注册成功！"



@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # print(request.form)
        user = request.form.get('username')
        password = request.form.get('password')
        print(user,password)
        return "登陆成功！"

if __name__ == '__main__':
    app.run()
