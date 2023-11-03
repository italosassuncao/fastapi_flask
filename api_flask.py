from flask_ngrok import run_with_ngrok
from flask import request
from flask import jsonify
from flask import Flask
import random as rk

app = Flask(__name__)
run_with_ngrok(app)

d = {
    "nome": "Italo",
    "sobrenome": "Silva",
    "idade": 27
}

@app.route("/")
def home():
  return "<marquee><h3> To check input add '/input' to the URL and to check output add '/output' to the URL.</h3>"

@app.route("/")
def input():
   return jsonify(d)

@app.route("/output", methods=['GET', 'POST'])

def predJson():
    pred = r.choice(["positive", "negative"])
    nd = d
    nd["prediction"]=pred
  
    return jsonify(nd)

app.run()
