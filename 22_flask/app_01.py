#!/usr/bin/python3
# Time: 2019/04/12 2:25 AM


"""about:
once installed flask, on terminator, type:
# flask

"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Hey!"


# user could be anything you want
@app.route('/great/<user>')
def feel(user):
    return "gooooooooooooooooooood!" + user


@app.route('/html')
def john():
    some_name = "heeihei"
    return render_template('base.html', name=some_name)
    # use some_name in html

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)



