from flask import Flask, render_template, request
from serpapi import GoogleSearch
import os
from dotenv import load_dotenv
import json
import re


app = Flask(__name__)
load_dotenv()


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
        
        results_key = re.search(r'\w*_(results)', " ".join(search.get_dict().keys()))
        results = search.get_dict()[results_key.group(0)]
        
    return render_template('results.html', results=results)
