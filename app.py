import os

from flask import Flask, render_template
import feedparser
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def fetch_openai_status():
    feed = feedparser.parse('https://status.openai.com/history.rss')
    entry = feed.entries[0]
    return {'name': 'OpenAI', 'status': entry.title, 'description': entry.summary}

def fetch_aws_status():
    # Implement AWS status fetching (example)
    return {'name': 'AWS', 'status': 'Operational', 'description': 'All systems normal.'}

# Similarly, implement fetch functions for HubSpot, Heroku, Gmail, Kinsta, Canva, and Webflow.

def get_all_statuses():
    services = []
    services.append(fetch_openai_status())
    services.append(fetch_aws_status())
    # Append other services
    return services

@app.route('/')
def index():
    services = get_all_statuses()
    return render_template('index.html', services=services)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
