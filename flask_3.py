from flask import Flask, request, render_template
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

@app.route('/')
def index():
    return 'Hello'

@app.route('/birthday', methods = ['POST','GET'])
def birthday():
    if request.method == 'POST':
        date = request.form.get('date').split('-') 
        return render_template('display_birthday.html',text=calc_next_birthday(int(date[0]),int(date[1]),int(date[2])))
    else:
        return render_template('birthday.html')

@app.route('/comment', methods = ['POST','GET'])
def comment():
    if request.method == 'POST':
        text = request.form.get('comment')
        return ''

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=80, debug=True)
