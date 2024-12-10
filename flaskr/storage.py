import os
import json


def save(data):
    """Save data to a json file
    """
    if os.path.exists('data.json'):
        with open('search_results.json', 'a') as file:
            json.dump(data, file)
    else:
        with open('search_results.json', 'w') as file:
            json.dump(data, file)
    
