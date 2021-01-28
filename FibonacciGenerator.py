from werkzeug.debug import DebuggedApplication
from flask import Flask,render_template,request
from jinja2 import Environment, PackageLoader
from flask import flash, redirect, url_for

app= Flask(__name__)
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

def fib(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fib(num-1)+fib(num-2)

@app.route('/',methods=["GET","POST"])
def hello_world():
    return render_template('view.html')

@app.route('/Fibresultview',methods=["GET","POST"])
def generate_fibonacci():
    number =int(request.form["userinput"])
    fibArray={}
    for x in range(number):
         fibArray[x]=fib(x)

    return render_template("Fibresultview.html",num=number,map=fibArray)

if __name__ =='__main__':
    app.run(host='127.0.0.1',debug=True,port=8000)

