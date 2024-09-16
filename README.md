# What's Up? - Service Status Dashboard

Hey there! Welcome to **What's Up?**, your friendly neighborhood dashboard that keeps tabs on the status of all your favorite services like OpenAI, AWS, HubSpot, Heroku, Gmail, Kinsta, Canva, and Webflow. If you're tired of jumping between different status pages, this app is about to make your life a whole lot easier.

![alt text](https://github.com/GTMDeltaTeam/whatsup/blob/main/static/images/.jpg/whatsup-screen.png?raw=true)

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the App Locally](#running-the-app-locally)
- [Deployment](#deployment)
  - [Deploying to Heroku](#deploying-to-heroku)
- [Contributing](#contributing)
- [License](#license)
- [Get in Touch](#get-in-touch)

---

## Getting Started

### Prerequisites

Before we dive in, make sure you've got the following set up:

- **Python 3.7+** - Because we're all about that modern Python life.
- **Git** - To clone the repo and contribute like a pro.
- **pip** - For managing Python packages.
- (Optional but highly recommended) **Virtualenv** - To keep your dependencies tidy.

### Installation

1. **Clone the Repository**

   Open up your terminal and run:

   ```bash
   git clone https://github.com/GTMDeltaTeam/whats-up-dashboard.git
   cd whats-up-dashboard
   ```

2. **Set Up a Virtual Environment**

   Let's keep things clean:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the Dependencies**

   Install all the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### Running the App Locally

Ready to see it in action? Let's fire it up:

```bash
python app.py
```

By default, the app runs on port **5000**. Open your favorite browser and navigate to `http://localhost:5000` to check it out.

Want to use a different port? No problem! Just set the `PORT` environment variable:

```bash
export PORT=8000  # On Windows use: set PORT=8000
python app.py
```

---

## Deployment

### Deploying to Heroku

Thinking about sharing this nifty dashboard with the world? Deploying to Heroku is a breeze.

1. **Install the Heroku CLI**

   If you haven't already, download and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

2. **Log In to Heroku**

   ```bash
   heroku login
   ```

3. **Create a New Heroku App**

   ```bash
   heroku create your-app-name
   ```

4. **Add a Procfile**

   In the root directory of your project, create a file named `Procfile` (no file extension) and add the following line:

   ```
   web: gunicorn app:app
   ```

   This tells Heroku how to run your app.

5. **Push to Heroku**

   ```bash
   git push heroku main
   ```

6. **Scale the Dynos**

   ```bash
   heroku ps:scale web=1
   ```

7. **Open Your App**

   ```bash
   heroku open
   ```

And voilà! Your app is live on Heroku.

---

## Contributing

First off, thanks for considering contributing! You're awesome.

Here's how you can get involved:

1. **Fork the Repository**

   Click the "Fork" button at the top right of this page to create your own copy of the repo.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/yourusername/whats-up-dashboard.git
   cd whats-up-dashboard
   ```

3. **Create a Branch**

   Keep your changes organized:

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Your Changes**

   Feel free to improve the code, fix bugs, or add new features.

5. **Commit Your Changes**

   ```bash
   git commit -m "Add some feature"
   ```

6. **Push to Your Fork**

   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**

   Head over to the original repo and open a pull request. Provide a brief description of your changes, and we'll review it ASAP.

---

## License

This project is licensed under the **MIT License**. Feel free to use it as you see fit.

---

## Get in Touch

Have questions, suggestions, or just want to say hi? Feel free to reach out!

- **Email:** [eric@gtmdelta.com](mailto:eric@gtmdelta.com)
- **Twitter:** [@DiscoPosse](https://twitter.com/DiscoPosse)
- **Website:** [https://gtmdelta.com](https://gtmdelta.com)

---

Thanks for checking out **What's Up?**! If you find this project helpful, give it a star ⭐️ and share it with others.

Happy coding!