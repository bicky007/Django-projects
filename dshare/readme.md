# DShare: A Django-Based File Sharing Platform

DShare is a Django-based web application that allows users to share files and text between devices using special keywords and a simple password-based login. The application features a dark theme and uses Tailwind CSS for styling.

## Features

- Simple password-based login (no username required)
- File upload and download using special keywords
- Clipboard text pasting support
- Dark theme using Tailwind CSS
- Easy deployment to PythonAnywhere

## Technologies Used

- Django
- Python
- Tailwind CSS
- JavaScript

## Setup Instructions

### Prerequisites

- Python 3.10 or later
- Virtual environment (recommended)
- Git

### Local Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/bicky007/dshare.git
    cd dshare
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the database**:

    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

6. **Access the application**:

    Open a web browser and go to `http://127.0.0.1:8000`.
