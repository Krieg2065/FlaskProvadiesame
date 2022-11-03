from flask import Flask, jsonify
from flask.ext.pymssql import PyMssql

app = Flask(__name__)
db = PyMssql(app)


@app.route("/login")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/user/<username>')
def user_detail(username):
    conn = pymssql.connect(host = r'213.140.22.237\SQLEXPRESS', user = r'elsherbini.mohamed',password= r'xxx123##', database= r'elsherbini.mohamed')
    cur = conn.cursor(as_dict=True)
    cursor.execute('SELECT * FROM users WHERE username=%s', username)
    user = cursor.fetchone()
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)