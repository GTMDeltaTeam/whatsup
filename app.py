import os

from flask import Flask, render_template
import feedparser
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_openai_status():
    try:
        feed = feedparser.parse('https://status.openai.com/history.rss')
        if feed.entries:
            entry = feed.entries[0]
            last_updated = datetime(*entry.published_parsed[:6]).strftime('%Y-%m-%d %H:%M:%S')
            return {
                'name': 'OpenAI',
                'status': entry.title,
                'description': entry.summary,
                'last_updated': last_updated
            }
        else:
            return {
                'name': 'OpenAI',
                'status': 'Operational',
                'description': 'All systems normal.',
                'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
    except Exception as e:
        logger.error(f"Error fetching OpenAI status: {e}")
        return {
            'name': 'OpenAI',
            'status': 'Unknown',
            'description': f'Error fetching status: {e}',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

def fetch_aws_status():
    try:
        feed = feedparser.parse('https://status.aws.amazon.com/rss/global.rss')
        if feed.entries:
            entry = feed.entries[0]
            status = entry.title
            description = entry.summary
            last_updated = datetime(*entry.published_parsed[:6]).strftime('%Y-%m-%d %H:%M:%S')
        else:
            status = "Operational"
            description = "All systems normal."
            last_updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'name': 'AWS', 'status': status, 'description': description, 'last_updated': last_updated}
    except Exception as e:
        logger.error(f"Error fetching AWS status: {e}")
        return {'name': 'AWS', 'status': 'Unknown', 'description': f'Error: {e}', 'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

def fetch_hubspot_status():
    try:
        feed = feedparser.parse('https://status.hubspot.com/history.rss')
        if feed.entries:
            entry = feed.entries[0]
            last_updated = datetime(*entry.published_parsed[:6]).strftime('%Y-%m-%d %H:%M:%S')
            return {'name': 'HubSpot', 'status': entry.title, 'description': entry.summary, 'last_updated': last_updated}
        else:
            return {'name': 'HubSpot', 'status': 'Operational', 'description': 'All systems normal.', 'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    except Exception as e:
        logger.error(f"Error fetching HubSpot status: {e}")
        return {'name': 'HubSpot', 'status': 'Unknown', 'description': f'Error: {e}', 'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

def fetch_heroku_status():
    try:
        feed = feedparser.parse('https://status.heroku.com/feed')
        if feed.entries:
            entry = feed.entries[0]
            last_updated = datetime(*entry.published_parsed[:6]).strftime('%Y-%m-%d %H:%M:%S')
            return {'name': 'Heroku', 'status': entry.title, 'description': entry.summary, 'last_updated': last_updated}
        else:
            return {'name': 'Heroku', 'status': 'Operational', 'description': 'All systems normal.', 'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    except Exception as e:
        logger.error(f"Error fetching Heroku status: {e}")
        return {'name': 'Heroku', 'status': 'Unknown', 'description': f'Error: {e}', 'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

def fetch_gmail_status():
    # Since scraping Google's status page may violate their terms of service,
    # we'll provide a link to their status dashboard instead.
    return {
        'name': 'Gmail',
        'status': 'See Status Page',
        'description': 'Visit the status page for current information.',
        'link': 'https://www.google.com/appsstatus/dashboard/',
        'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

def fetch_kinsta_status():
    try:
        response = requests.get('https://status.kinsta.com/')
        soup = BeautifulSoup(response.content, 'html.parser')
        status_element = soup.find('span', class_='page-status-indicator-status')
        status = status_element.text.strip() if status_element else "Unknown"
        description_element = soup.find('div', class_='actual-status-description')
        description = description_element.text.strip() if description_element else "No description available."
        return {
            'name': 'Kinsta',
            'status': status,
            'description': description,
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    except Exception as e:
        logger.error(f"Error fetching Kinsta status: {e}")
        return {
            'name': 'Kinsta',
            'status': 'Unknown',
            'description': f'Error fetching status: {e}',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

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
        return {
            'name': 'Canva',
            'status': status,
            'description': description,
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    except Exception as e:
        logger.error(f"Error fetching Canva status: {e}")
        return {
            'name': 'Canva',
            'status': 'Unknown',
            'description': f'Error fetching status: {e}',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

def fetch_webflow_status():
    try:
        feed = feedparser.parse('https://status.webflow.com/history.rss')
        if feed.entries:
            entry = feed.entries[0]
            last_updated = datetime(*entry.published_parsed[:6]).strftime('%Y-%m-%d %H:%M:%S')
            return {'name': 'Webflow', 'status': entry.title, 'description': entry.summary, 'last_updated': last_updated}
        else:
            return {'name': 'Webflow', 'status': 'Operational', 'description': 'All systems normal.', 'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    except Exception as e:
        logger.error(f"Error fetching Webflow status: {e}")
        return {'name': 'Webflow', 'status': 'Unknown', 'description': f'Error: {e}', 'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

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
    port = int(os.environ.get('PORT', 3002))
    app.run(debug=True, host='0.0.0.0', port=port)
