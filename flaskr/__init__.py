from flask import Flask, render_template, request
import serpapi
import os


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['GET', 'POST'])
def search(q: str = ''):
    if request.method == 'POST':
        q = request.form.get('search_query')
        params = {
            'q': q,
            'engine': 'google',
            'api_key': os.environ.get('SERP_API_KEY')
        }
        search = GoogleSearch(params)
        
    return render_template('results.html', results=search.get_dict())
