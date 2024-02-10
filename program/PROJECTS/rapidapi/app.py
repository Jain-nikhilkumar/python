from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace with your actual RapidAPI key
RAPIDAPI_KEY = "2a647829f4mshaaa7d32c83585b7p13f113jsn5dc76c090e4b"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_metadata', methods=['POST'])
def fetch_metadata():
    try:
        # Get the URL submitted by the user
        url = request.form.get('url')

        # Make a request to the OpenGraph.io API
        headers = {
            "X-RapidAPI-Key": "2a647829f4mshaaa7d32c83585b7p13f113jsn5dc76c090e4b",
            "X-RapidAPI-Host": "opengraph-io.p.rapidapi.com"
        }
        querystring = {
            "url": url,
            "accept_lang": "en-US,en;q=0.9",
            "full_render": "false",
            "cache_ok": "false",
            "max_cache_age": "432000000"
        }

        response = requests.get(
            "https://opengraph-io.p.rapidapi.com/api/1.1/sites",
            headers=headers,
            params=querystring
        )

        response_data = response.json()

        # Extract OpenGraph metadata
        title = response_data.get('title', '')
        description = response_data.get('description', '')
        image_url = response_data.get('image', '')

        return render_template('metadata.html', title=title, description=description, image_url=image_url)

    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
