from flask import Flask, redirect, request, render_template, url_for
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('comment'))

@app.route('/comment', methods=['POST', 'GET'])
def comment():
    if request.method == 'POST':
        name = request.form['name']
        title = request.form['title']
        content = request.form['content']
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        if name and title and content:
            with open('comment_db.txt', 'a') as file:
                file.write(f"{timestamp} | {name} | {title} | {content}\n")
        return redirect('/comment')

    try: 
        with open('comment_db.txt', 'r') as file:
            comment_list = [line.strip().split(' | ') for line in file.readlines()]
            return render_template('comment_page.html', comment_list=comment_list)
    except:
        return render_template('comment_page.html', comment_list=[])

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=80, debug=True)
