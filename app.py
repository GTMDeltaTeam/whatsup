from flask import Flask, render_template
import feedparser
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

def fetch_openai_status():
    feed = feedparser.parse('https://status.openai.com/history.rss')
    if feed.entries:
        entry = feed.entries[0]
        return {'name': 'OpenAI', 'status': entry.title, 'description': entry.summary}
    else:
        return {'name': 'OpenAI', 'status': 'Operational', 'description': 'All systems normal.'}

def fetch_aws_status():
    feed = feedparser.parse('https://status.aws.amazon.com/rss/global.rss')
    if feed.entries:
        entry = feed.entries[0]
        status = entry.title
        description = entry.summary
    else:
        status = "Operational"
        description = "All systems normal."
    return {'name': 'AWS', 'status': status, 'description': description}

def fetch_hubspot_status():
    feed = feedparser.parse('https://status.hubspot.com/history.rss')
    if feed.entries:
        entry = feed.entries[0]
        return {'name': 'HubSpot', 'status': entry.title, 'description': entry.summary}
    else:
        return {'name': 'HubSpot', 'status': 'Operational', 'description': 'All systems normal.'}

def fetch_heroku_status():
    feed = feedparser.parse('https://status.heroku.com/feed')
    if feed.entries:
        entry = feed.entries[0]
        return {'name': 'Heroku', 'status': entry.title, 'description': entry.summary}
    else:
        return {'name': 'Heroku', 'status': 'Operational', 'description': 'All systems normal.'}

def fetch_gmail_status():
    return {
        'name': 'Gmail',
        'status': 'See Status Page',
        'description': 'Visit the status page for current information.',
        'link': 'https://www.google.com/appsstatus/dashboard/'
    }

def fetch_kinsta_status():
    try:
        response = requests.get('https://status.kinsta.com/')
        soup = BeautifulSoup(response.content, 'html.parser')
        status_element = soup.find('span', class_='page-status-indicator-status')
        status = status_element.text.strip() if status_element else "Unknown"
        description = "Kinsta status fetched successfully."
    except Exception as e:
        status = "Unknown"
        description = f"Error fetching status: {e}"
    return {'name': 'Kinsta', 'status': status, 'description': description}

def fetch_canva_status():
    try:
        response = requests.get('https://canvastatus.com/')
        soup = BeautifulSoup(response.content, 'html.parser')
        status_element = soup.find('div', class_='page-status')
        if status_element:
            status = status_element.find('span').text.strip()
            description = status_element.find('p').text.strip()
        else:
            status = "Operational"
            description = "All systems normal."
    except Exception as e:
        status = "Unknown"
        description = f"Error fetching status: {e}"
    return {'name': 'Canva', 'status': status, 'description': description}

def fetch_webflow_status():
    feed = feedparser.parse('https://status.webflow.com/history.rss')
    if feed.entries:
        entry = feed.entries[0]
        return {'name': 'Webflow', 'status': entry.title, 'description': entry.summary}
    else:
        return {'name': 'Webflow', 'status': 'Operational', 'description': 'All systems normal.'}

def get_all_statuses():
    services = []
    services.append(fetch_openai_status())
    services.append(fetch_aws_status())
    services.append(fetch_hubspot_status())
    services.append(fetch_heroku_status())
    services.append(fetch_gmail_status())
    services.append(fetch_kinsta_status())
    services.append(fetch_canva_status())
    services.append(fetch_webflow_status())
    return services

@app.route('/')
def index():
    services = get_all_statuses()
    return render_template('index.html', services=services)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
