import os
from flask import Flask, render_template,url_for
from api import app2

def create_app():
    app = Flask(__name__,static_folder="./static",template_folder="./templates")
    app.register_blueprint(app2)
    return app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index2')
def index2():
    return url_for('index')

if __name__ == '__main__':
    app.run()
