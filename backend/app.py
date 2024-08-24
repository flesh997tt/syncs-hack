from flask import Flask
from backend import Backend

app = Flask(__name__)
backend = Backend('backend/data.txt')

if __name__ == '__main__':
    app.run(debug=True)