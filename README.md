# Job Applicant Dashboard

This is a Django web application designed to serve as a Job Applicant Dashboard specifically for the "Junior Developer" position. It allows you to manage applicant information, portfolios, and projects through the Django Admin interface and provides a user-friendly dashboard for viewing and managing applicants.

## Features

* **Applicant Listing:** A table displaying basic information (first name, last name, email) of Junior Developer applicants.
* **Detailed Portfolio View:** A dedicated page to view an applicant's full portfolio and associated project details.
* **Applicant Management:**
    * **Go:** Redirects to the detailed portfolio page.
    * **Delete:** Deletes an applicant and their associated portfolio and project from the database.
* **Django Admin Integration:** All data (Users, Portfolios, Projects) can be managed and created directly within the Django Admin.
* **Static CDN for Bootstrap:** Bootstrap is served as a static file from your project.
* **Django Template Tags:** Utilizes `{% extends %}`, `{% include %}`, `{% url %}` for efficient templating.

## Project Structure

djangoProject4/
├── djangoProject4/          # Main Django project settings
├── portfolio/              # Django app for portfolio and applicant management
├── static/                 # Static files (e.g., Bootstrap CSS)
├── templates/              # HTML templates for the application
├── manage.py               # Django's command-line utility
├── README.md               # This file
└── .gitignore              # Git ignore file

## Getting Started

### Prerequisites

* Python 3.8+
* pip (Python package installer)

### 1. Clone the Repository

```bash
git clone https://github.com/jcg0807/djangoProject4.git
cd djangoProject4

2. Create and Activate a Virtual Environment
bash

python -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

3. Install Dependencies
bash

pip install Django

4. Download Bootstrap

Download the compiled CSS for Bootstrap (bootstrap.min.css) from getbootstrap.com and place it in:
text

djangoProject4/portfolio/static/css/bootstrap.min.css

5. Run Database Migrations
bash

python manage.py makemigrations portfolio
python manage.py migrate

6. Create a Superuser
bash

python manage.py createsuperuser

7. Run the Development Server
bash

python manage.py runserver

Access the application at: http://127.0.0.1:8000/
Usage
Django Admin

    Access: http://127.0.0.1:8000/admin/

    Create:

        Users (under Authentication and Authorization)

        Projects (under Portfolio)

        Portfolios (link Users to Projects)

Applicant Dashboard

    Main view: http://127.0.0.1:8000/

    Portfolio detail: http://127.0.0.1:8000/portfolio/<username>/
