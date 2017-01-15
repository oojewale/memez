from flask import Flask, render_template, views, request
from routes import setup_routes

app = Flask(__name__)

setup_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
