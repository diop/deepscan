import os
import sys
from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def main():
    return 'Superscan - Medical Imaging x Deep Learning'

if __name__ == '__main__':
    app.run()