from flask import Flask, render_template
from dotenv import load_dotenv
import os


app = Flask(__name__)

load_dotenv()

params = {
    'engine': 'google',
    'api_key': os.environ.get('SERP_API_KEY'),
    'q': 'weather today'
}


@app.route('/')
def index():
    return render_template('index.html')


return app
