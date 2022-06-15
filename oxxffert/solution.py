#!/usr/bin/python3


# from distutils.log import debug
# from crypt import methods
# from unittest import result
# from crypt import methods
import flask
from flask import Flask , render_template
from flask import request
import sys 
import math
import json
import sympy as sym 
from sympy import *
from sympy.abc import *
import os 

# from numpy import char 


app = Flask(__name__)
@app.route('/')
def main():
    return render_template("index.html")



@app.route('/clubsters', methods=["POST"])
def clubsters():
    if request.method == "POST":
        charger = request.form["value_1"]
        #evaluator = str(request.form['result'])
        def buildman(operation):
            
            mmmaker =  eval(operation)
            # print(mmmaker)
            # if str(operation):
            # buildman(eval("operation"))

                # print(f'result --> {make}')
        # buildman(charger)
        # operr = buildman--(charger)
        if str(charger):
            make = eval(charger)
            print(float(make))
            return render_template("index.html", result=float(make))
        # return render_template("index.html", )
    # pass
@app.route('/strangerman', methods=["POST"])
def strangerman():
    if request.method == "POST":
        kwork = int(request.form["sq_raiz"])
        if int(kwork):
            pth = math.sqrt(kwork)          
            return render_template('index.html', ravengold=pth)



@app.route('/integrals', methods=["POST"])
def integrals():
    if request.method == "POST":
        composer = request.form["ingral_1"]
        voold =  request.form["verify"]
        def brainsolver(example):
            x , y, z = sym.symbols('x, y , z')
            w , t , u =  sym.symbols('w, t, u')
            v, s, a , b = sym.symbols('v , s, a, b')

            igral = integrate(example)
            # print(igral)
        # brainsolver(composer)
        aproved = brainsolver(composer)
        print(aproved)
        def brainderive(exaout):
            x , y, z = sym.symbols('x y z')
            w , t , u =  sym.symbols('w  t u')
            v, s, a , b = sym.symbols('v s a b')
            init_printing(use_unicode=True)
            igral = diff(exaout)
            igral
        # new_val = brainderive(composer)

        # if int(composer):
        #     pass

        if  voold == "integral":
            return render_template('index.html', hoolview=aproved)
        elif voold == "derivate":
            return render_template('index.html', hoolview=composer)



@app.route('/saveme', methods=["POST"])
def saveme( assembly , declif ):
    updat_file = os.join('loggin.txt')
    alice = open(updat_file, 'w')
    chunck = 0
    dumping = request.form[assembly]

    for z in alice:
        chunck += 1
        z.write('#[chunck] --> dumping %H:%M:%S \n')
        # print(z)

app.run(debug=True, port=5633 ) 
if __name__ == "__main__":
    clubsters()
    strangerman()
    main()
    # pass