from flask import (
    Flask,
    render_template)

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('home.html')

if __name__ == '__main__':
    app.secret_key = 'My Key'
    app.run(debug=True)
