from flask import Flask, render_template, request

app = Flask(__name__)# interface between my server and my application wsgi

import pickle
model = pickle.load(open(r'C:\Users\annab\Downloads\vipul\model1.pkl','rb'))

@app.route('/')#binds to an url
def helloworld():
    return render_template("index.html")

@app.route('/login', methods =['POST'])#binds to an url
def login():
    p =request.form['HDI']
    v1=request.form['Total Deaths']
    v2=request.form['Stringency Index']
    v3=request.form['Population']
    v4=request.form['GDP Before Covid']
    v5=request.form['GDP During Covid']
    t=[[float(p),float(v1),float(v2),float(v3),float(v4),float(v5)]]
    output= model.predict(t)
    return render_template("index.html",y =  float(output ))
    


if __name__ == '__main__' :
    app.run(debug= False)# -*- coding: utf-8 -*-

