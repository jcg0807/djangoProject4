# Junior Developer Applicant Portal

This Django application serves as a management system for tracking candidates applying for Junior Developer positions. The platform enables administrators to organize applicant portfolios and associated projects through an intuitive interface.

## Key Functionality

* **Candidate Overview:** Displays applicant details including names and contact information in a structured table format
* **Portfolio Inspection:** Provides comprehensive views of each candidate's work samples and project history
* **Candidate Administration:**
    * **View:** Access complete portfolio details
    * **Remove:** Delete applicant records along with related materials
* **Administration Panel:** Full control over user accounts, portfolios, and projects through Django's built-in admin
* **Local Bootstrap:** Bootstrap framework hosted within the project files
* **Template Organization:** Efficient template structure using Django's template system

## Directory Layout
djangoProject4/
├── djangoProject4/ # Core configuration files
├── portfolio/ # Application components
├── static/ # CSS and JavaScript assets
├── templates/ # Interface templates
├── manage.py # Project control script
├── README.md # Documentation
└── .gitignore # Version control exclusions

## Setup Instructions

### Requirements

* Python 3.8 or newer
* pip package manager

### 1. Obtain Project Files

```bash
git clone https://github.com/jcg0807/djangoProject4.git
cd djangoProject4
```
2. Configure Virtual Environment
```bash
python -m venv venv

# macOS/Linux activation:
source venv/bin/activate

# Windows activation:
venv\Scripts\activate
```
3. Install Required Packages
 ```bash
pip install Django
```
4. Set Up Bootstrap

    Download Bootstrap CSS from the official site

    Place the file at:
djangoProject4/portfolio/static/css/bootstrap.min.css

5. Prepare Database
```bash
python manage.py makemigrations portfolio
python manage.py migrate
```
6. Create Administrator Account
```bash
python manage.py createsuperuser
```
7. Launch Application
```bash
python manage.py runserver
```
Access the system at: http://127.0.0.1:8000/
How to Use
Administration Console

    Navigate to http://127.0.0.1:8000/admin/

    Manage:

        User accounts

        Development projects

        Candidate portfolios

Applicant Interface

    Main dashboard: http://127.0.0.1:8000/

    Individual portfolios: http://127.0.0.1:8000/portfolio/[username]/

System Architecture

    Data Models:

        Portfolio (Direct association with User)

        Project (Flexible relationship with Portfolios)

    View Components:

        Listing view (Functional approach)

        Detailed view (Class-based)

        Removal view (Class-based)

    Address Routing: Utilizes usernames in paths (/portfolio/[username]/)
