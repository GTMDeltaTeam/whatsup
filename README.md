# whatsup

**Step-by-Step Guide to Building and Deploying "What's Up?" Status Dashboard on Heroku**

---

### **Table of Contents**

1. [Requirements](#requirements)
2. [Build Process](#build-process)
   - [Project Setup](#project-setup)
   - [Fetching Service Statuses](#fetching-service-statuses)
   - [Designing the Frontend](#designing-the-frontend)
   - [Implementing Auto-Refresh](#implementing-auto-refresh)
3. [Deployment to Heroku](#deployment-to-heroku)
   - [Preparing for Deployment](#preparing-for-deployment)
   - [Deploying the App](#deploying-the-app)
   - [Setting Up Custom Domain](#setting-up-custom-domain)
4. [Final Notes](#final-notes)

---

## **Requirements**

### **Software and Tools**

- **Python 3.8+**: Programming language for backend development.
- **Flask**: Lightweight web application framework.
- **Feedparser**: Library for parsing RSS feeds.
- **Requests**: Library for making HTTP requests.
- **BeautifulSoup4**: Library for web scraping.
- **Gunicorn**: WSGI HTTP server for UNIX.
- **Heroku CLI**: Command-line interface for Heroku.

### **Dependencies**

Create a `requirements.txt` file with the following contents:

```plaintext
Flask==2.1.1
feedparser==6.0.8
requests==2.27.1
beautifulsoup4==4.10.0
gunicorn==20.1.0
```

---

## **Build Process**

### **1. Project Setup**

#### **a. Create Project Directory**

```bash
mkdir whats-up-dashboard
cd whats-up-dashboard
```

#### **b. Set Up a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

#### **c. Install Dependencies**

```bash
pip install -r requirements.txt
```

#### **d. Project Structure**

```plaintext
whats-up-dashboard/
├── app.py
├── requirements.txt
├── Procfile
├── templates/
│   └── index.html
├── static/
    ├── css/
    │   └── styles.css
    └── js/
        └── scripts.js
```

### **2. Fetching Service Statuses**

Create `app.py` and include functions to fetch statuses for each service.

```python
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
    app.run(debug=True)
```

### **3. Designing the Frontend**

#### **a. HTML Template (`templates/index.html`)**

Create a modern tiled view using Bootstrap for styling.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>What's Up? - Service Status Dashboard</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Auto Refresh every 5 minutes -->
    <meta http-equiv="refresh" content="300">
</head>
<body>
    <div class="container">
        <h1 class="my-4 text-center">What's Up?</h1>
        <div class="row">
            {% for service in services %}
            <div class="col-md-4">
                <div class="card mb-4 shadow-sm">
                    <div class="card-body">
                        <h5 class="card-title">{{ service.name }}</h5>
                        <p class="card-text">{{ service.status }}</p>
                        <p class="card-text"><small>{{ service.description }}</small></p>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <!-- Custom JS -->
    <script src="{{ url_for('static', filename='js/scripts.js') }}"></script>
</body>
</html>
```

#### **b. CSS Styling (`static/css/styles.css`)**

Add custom styles if needed.

```css
body {
    background-color: #f8f9fa;
}
h1 {
    font-family: 'Arial', sans-serif;
}
```

#### **c. JavaScript (Optional, `static/js/scripts.js`)**

If additional interactivity is required.

### **4. Implementing Auto-Refresh**

The `<meta>` tag in the HTML template ensures the page refreshes every 5 minutes.

---

## **Deployment to Heroku**

### **1. Preparing for Deployment**

#### **a. Procfile**

Create a `Procfile` to specify how to run the app.

```plaintext
web: gunicorn app:app
```

#### **b. Update `app.py` for Heroku**

Ensure the app listens on the port provided by Heroku.

```python
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```
### **2. Deploying the App**

#### **a. Login to Heroku**

```bash
heroku login
```

#### **b. Create Heroku App**

```bash
heroku create whatsup-dashboard
```

#### **c. Set Buildpacks (Optional)**

Heroku automatically detects Python apps, but you can specify:

```bash
heroku buildpacks:set heroku/python
```

#### **d. Deploy to Heroku**

```bash
git push heroku main  # Use 'master' if your default branch is master
```

#### **e. Scale the App**

```bash
heroku ps:scale web=1
```

#### **f. Open the App**

```bash
heroku open
```

### **3. Setting Up Custom Domain**

#### **a. Add Custom Domain**

```bash
heroku domains:add whatsup.gtmdelta.com
```

Heroku will provide a DNS target, something like `whatsup-dashboard.herokuapp.com`.

#### **b. Configure DNS**

- Go to your domain registrar's DNS settings.
- Create a **CNAME** record:
  - **Host/Alias/Name**: `whatsup`
  - **Value/Points to**: `whatsup-dashboard.herokuapp.com`
  - **TTL**: Default or 3600 seconds

#### **c. Verify Domain**

```bash
heroku domains
```

Wait for DNS changes to propagate (may take up to 24 hours but usually faster).

#### **d. Secure the Domain (Enable SSL)**

Heroku automatically provisions SSL certificates for custom domains.

```bash
heroku certs:auto:enable
```

---

## **Final Notes**

- **Auto-Refresh**: The dashboard refreshes every 5 minutes to fetch the latest statuses.
- **Responsive Design**: Using Bootstrap ensures the dashboard is mobile-friendly.
- **Error Handling**: Implement try-except blocks in your fetch functions to handle exceptions gracefully.
- **Caching (Optional)**: To improve performance, consider caching the fetched data for a short duration.
- **Heroku Scheduler (Optional)**: Use the Heroku Scheduler add-on for background tasks if needed.

---

**Congratulations!** You have successfully built and deployed the "What's Up?" status dashboard on Heroku with a custom domain.

---

### **Additional Tips**

- **Logging**: Use Python's `logging` module to log errors and important events.
- **Monitoring**: Keep an eye on your app's performance via Heroku's dashboard.
- **Scaling**: If needed, you can scale your app vertically by adding more dynos.
- **Updates**: Regularly update your dependencies to patch security vulnerabilities.

---

**Disclaimer**: Ensure you comply with each service's terms of service when fetching their status information. Avoid scraping if an API or RSS feed is available.