# Django To-Do List Application

A simple To-Do list application built with Django, allowing users to create, update, delete, and view tasks. The application uses Django Crispy Forms for improved form styling and Bootstrap for front-end design.

## Features

- Add new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as completed
- Responsive UI with Bootstrap

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or higher
- pip (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/bicky007/todo-django.git
cd todo-django
```

### Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```

### Install Dependencies
```bash
Python 3.x
Django 3.x or higher
pip (Python package installer)
crispy-bootstrap4
django-crispy-forms
```

### Apply Migrations
```bash
python manage.py migrate
```
### Run Server
```bash
python manage.py runserver
```
## Project Structure
```bash
todo-django/
├── todo/
│   ├── migrations/
│   ├── templates/
│   │   ├── delete_task.html
│   │   ├── index.html
│   │   └── update_task.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── todo_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```

## Project Screenshots
![Screenshot 2024-05-26 230015](https://github.com/bicky007/Django-projects/assets/128511616/9f16a579-aa79-42ee-b6e9-83de1b5aefa8)
![Screenshot 2024-05-26 230028](https://github.com/bicky007/Django-projects/assets/128511616/f4aa1ae6-027e-4e80-a2c1-a6ba9403df32)
![Screenshot 2024-05-26 230039](https://github.com/bicky007/Django-projects/assets/128511616/2179605b-dd93-466f-8205-f4f0bbaf4e96)
