from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<n>')
def greet(n=''):
    return render_template('hello.html', name='rng')

@app.route('/')
def index():
    return 'This is a website!'
    
@app.route('/')
@app.route('/getname', methods = ['POST', 'GET'])
def get_name():
    if request.method == 'POST':
        typed_name = request.form['name']
    else:
        typed_name = ''

    return render_template('hello_form.html', name=typed_name)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=80, debug=True)
