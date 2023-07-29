from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')

def homePage():

    return "Welcome to hidden Leaf Village"

@app.route('/calc',methods=['Get'])

def math_operator():

#getting request from postman
    number1 = request.json('number1')
    number2 = request.json('number2')
    operation = request.json('operation')

    operation=operation.upper()
    if operation == 'ADD'
        result = number1+number2

    if operation == 'SUB'
        result = number1-number2

        if operation == 'ADD'
        result = number1+number2

    if operation == 'DIV'
         result = number1/number2

print(__name__)

if __name__ == '__main__':
    app.run()
