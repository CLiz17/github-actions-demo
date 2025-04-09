from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/<random_string>')
# This function takes a string as input and returns it in reverse order.
def return_backwards_string(random_string):
    return random_string[::-1]

@app.route('/get_mode')
def get_mode():
    return os.environ.get("MODE")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)