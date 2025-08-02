from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')# main page 
def greet():
    return('Hello World')

@app.route('/greet1', methods = ['GET']) # instead of '/'
def greet1():
    return('Hellogood morning')

@app.route('/greet2', methods = ['POST']) # instead of '/'
def greet2():
    return('Hello good Afternoon')

@app.route('/greet3/<name>', methods = ['GET'])
def greet3(name):
    return(f"my name is {name}")

@app.route('/add1/<int:a>/<int:b>')
def add1(a,b):
    return(f"The addition of {a} and {b} is {a+b}")

@app.route('/add2') # instead of '/'
def add2():
    a = request.args.get('num1', type = int)
    b = request.args.get('num2', type = int) 
    return(f'The addition of {a} and {b} is {a+b}')

if __name__ == "__main__":
    app.run(debug  = True)
    




