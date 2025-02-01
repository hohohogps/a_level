from flask import Flask
from flask import request
import datetime

def calc_next_birthday(year,month,day):
    dob = datetime.date(year,month,day)
    today = datetime.date.today()

    print("My date of birth is: ", dob)
    print("Today is: ", today)
    birthday_this_year = datetime.date(today.year, dob.month, dob.day)
    birthday_next_year = datetime.date(today.year+1, dob.month, dob.day)

    if birthday_this_year > today:
        next_birthday = birthday_this_year
    else:
        next_birthday = birthday_next_year

    days_to_birthday = (next_birthday - today).days
    age = (next_birthday - dob).days // 365   
    return f'Next birthday: {next_birthday} <p> Days to next birthday: {days_to_birthday} <p> Age at next birthday: {age}'




app = Flask(__name__)



@app.route('/hello')
def hello():
    return f'Hello anonymous person.'

@app.route('/hello/<name>')
def greet(name):
    return f'Hello there, {name}'

@app.route('/')
def add():
    year = int(request.args.get('year', ''))
    month = int(request.args.get('month', ''))
    day = int(request.args.get('day', ''))
    return calc_next_birthday(year,month,day)
    


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=80, debug=True)
