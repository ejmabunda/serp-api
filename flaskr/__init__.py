from flask import Flask, render_template, request
import serpapi
import os
from dotenv import load_dotenv
import json
import re
from flaskr.storage import save


app = Flask(__name__)
load_dotenv()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['GET', 'POST'])
def results(q: str = ''):
    if request.method == 'POST':
        q = request.form.get('search')

        params = {
            'q': q,
            'engine': 'google',
            'api_key': os.environ.get('SERP_API_KEY')
        }
        # search = serpapi.search(params)
        # search_dict = search.as_dict()
        # # Save to a json file
        # save(search_dict)

        with open('search_results.json', 'r') as file:
            search_dict = json.load(file)
        
        organic_results = search_dict['organic_results']
        print(organic_results)
        
    return render_template('results.html', o_res=organic_results)
