from flask import Flask,request

app=Flask(__name__)

@app.route('/')

def homePage():

    return 'Welcome to hidden Leaf Village'

@app.route('/calc',methods=['Get'])

def math_operator():

#getting request from postman
    operation = request.json['operation']
    number1 = request.json['number1']
    number2 = request.json['number2']

    operation=operation.upper()
    
    if operation == 'ADD':
        result = int(number1) + int(number2)
        return f"The  addition of {number1} and {number2} is {result}"

    elif operation == 'SUB':
        result = int(number1) - int(number2)
        return f"The  subtraction of {number1} and {number2} is {result}"
    
    elif operation == 'MUL':
        result = int(number1) * int(number2)
        return f"The  multiplication of {number1} and {number2} is {result}"
    
    elif operation == 'DIV':
        result = int(number1) / int(number2)
        return f"The  division of {number1} and {number2} is {result}"
    else:
        return "Invalid Operation"
    

print(__name__)

if __name__ == '__main__':
    app.run()
