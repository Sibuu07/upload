import argparse
import json
import urllib.request
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/limited-array')
def get_limited_array():
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--limit', type=int, default=10,
                        help='Limit the number of items in the array')
    parser.add_argument('-u', '--url', required=True,
                        help='URL of the JSON file')
    args = parser.parse_args()

    # Fetch the JSON data from the URL
    with urllib.request.urlopen(args.url) as response:
        data = json.loads(response.read().decode())

    # Get the array you want to limit
    array_to_limit = data['array_to_limit']

    # Limit the array to a certain number of items
    limited_array = array_to_limit[:args.limit]

    # Convert the limited array to JSON format
    json_data = json.dumps(limited_array)

    # Return the limited array as JSON data
    return jsonify(json_data)

if __name__ == '__main__':
    app.run()
