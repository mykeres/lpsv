# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# /// <- relative path
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')
#   return '🛠🛠️ Página en construcción 🛠️🛠️'

if __name__ == "__main__":
    app.run(debug=True)
