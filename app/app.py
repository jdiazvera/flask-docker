from flask import Flask, jsonify, request 
from random import seed
from random import randint

app = Flask(__name__)

@app.route('/entero', methods=["GET"])
def get_entero():
    seed(1)
    result = randint(0, 10)
    return jsonify(value=result)

