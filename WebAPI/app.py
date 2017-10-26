from flask import Flask
from flask import render_template
import sqlit3

DATABASE = 'database.db'

def get_db():
    

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('layout.html')


if __name__ == '__main__':
    app.run(debug=True)