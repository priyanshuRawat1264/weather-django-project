# Weather App using Django

A beginner-friendly Django weather application developed as a practical project for the Django assignment.

## Project Reference

This project is based on the **Weather App using Django | Python** project listed under the beginner Django projects on GeeksforGeeks:

https://www.geeksforgeeks.org/python/django-projects/

The application is implemented as a working Django project with a SQLite database, Django ORM, templates, URL routing, form handling, API integration, error handling, and search-history storage.

## Features

- Search weather by city name
- Fetch live weather information from OpenWeatherMap
- Display city, country, temperature, humidity, pressure, description, and weather icon
- Store successful searches in SQLite using a Django model
- Display the five most recent searches
- Django Admin support for viewing search history
- Handles empty input, invalid cities, API/network errors, and missing API keys
- Includes sample database data for classroom demonstration
- Includes basic automated tests
- Responsive HTML/CSS interface

## Technologies Used

- Python 3
- Django 5.2+
- SQLite3
- HTML5 and CSS3
- Requests library
- OpenWeatherMap API
- Git and GitHub

## Project Structure

```text
weather_django_assignment/
├── manage.py
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
├── weather/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── main/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    │   ├── __init__.py
    │   └── 0001_initial.py
    ├── fixtures/
    │   └── sample_data.json
    └── templates/
        └── main/
            └── index.html
```

## Setup on Windows

### 1. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Apply migrations

```bash
python manage.py migrate
```

### 4. Load sample data

```bash
python manage.py loaddata sample_data
```

The sample data gives you records to demonstrate the **Recent Searches** section even before making live API searches.

### 5. Configure the OpenWeatherMap API key

Create an API key from OpenWeatherMap and set it as an environment variable.

PowerShell:

```powershell
$env:OPENWEATHER_API_KEY="YOUR_API_KEY"
```

Command Prompt:

```cmd
set OPENWEATHER_API_KEY=YOUR_API_KEY
```

Do **not** commit a real API key to GitHub.

### 6. Run the project

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Admin Panel

Create an admin user if required:

```bash
python manage.py createsuperuser
```

Then open:

```text
http://127.0.0.1:8000/admin/
```

The `SearchHistory` model is registered in Django Admin.

## Testing

Run the automated tests with:

```bash
python manage.py test
```

The tests cover:

- Home page loading
- Empty city validation
- Successful API search and database storage

## How the Project Works

1. The user enters a city name in the HTML form.
2. Django receives the POST request in `main/views.py`.
3. The view validates the input and sends a request to the OpenWeatherMap API.
4. The API response is converted into a Python dictionary used by the template.
5. Successful searches are saved in the `SearchHistory` Django model.
6. The template displays the current weather and recent searches.
7. Django ORM is used to retrieve the five latest searches from SQLite.

## Important Files

- `main/models.py` — defines the `SearchHistory` database model.
- `main/views.py` — handles requests, API calls, validation, errors, and database storage.
- `main/urls.py` — maps the home URL to the weather view.
- `main/templates/main/index.html` — user interface.
- `main/admin.py` — registers the model with Django Admin.
- `main/tests.py` — basic automated tests.
- `main/fixtures/sample_data.json` — sample records for demonstration.
- `weather/settings.py` — Django configuration and SQLite database setup.

## Assignment Checklist

- [x] Selected a Django project from the GeeksforGeeks Django Projects list
- [x] Implemented the project using Django
- [x] Added database/model functionality
- [x] Added sample data
- [x] Added a working user interface
- [x] Added error handling
- [x] Added README.md
- [x] Added requirements.txt
- [x] Added tests
- [x] Prepared the project for GitHub upload

## Note

The API key is intentionally not included in this repository. Each user should configure their own OpenWeatherMap API key locally.
