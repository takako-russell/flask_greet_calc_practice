# Put your app in here.
from flask import Flask, request
from operations import add,sub,mult,div

app = Flask(__name__)

@app.route("/add")
def addition():

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = add(a,b)
    return str(result)

@app.route("/sub")
def subtract():

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = sub(a,b)
    return str(result)

@app.route("/mult")
def multiply():

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = mult(a,b)
    return str(result)

@app.route("/div")
def divide():

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = div(a,b)
    return str(result)

@app.route("/math/<math>")
def do_culc(math):

    operations = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }
    
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(operations[math](a,b))