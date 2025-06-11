# PUST Career and Entrepreneurship Club Website

A full-stack web application developed using Django, HTML, CSS, Bootstrap, and PostgreSQL. This project serves as a practical demo for applying real-world web development skills.

## Features

- Responsive design with Bootstrap
- Dynamic content management with Django
- PostgreSQL database backend
- Deployed on Render.com

## Technologies Used

- Python, Django
- HTML, CSS, Bootstrap
- PostgreSQL
- Render.com

## Setup Instructions

```bash
git clone https://github.com/MH-Rokon/PUSTCEC.git
cd pust-career-club
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
