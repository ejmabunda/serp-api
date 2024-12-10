from flask import Flask, render_template, request
from serpapi import GoogleSearch
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
        search = GoogleSearch(params)
        search_dict = search.get_dict()
        # Save to a json file
        save(search_dict)
        
        organic_results = search_dict['organic_results']
        knowledge_graph = search_dict['knowledge_graph']
        
    return render_template('results.html',
                           organic_results=organic_results,
                           knowledge_graph=knowledge_graph)
