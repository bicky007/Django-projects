# Django Resume Builder

A Django-based web application to create, view, and download professional resumes.

## Features

- **Single Form for Resume Details:** Enter all necessary details like personal information, education, experience, certifications, projects, and skills in a single form.
- **View and Download Resume:** View the created resume in a professional format and download it as a PDF.

## Requirements

- Python 3.x
- Django 3.x or later
- WeasyPrint

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/bicky007/django-resume-builder.git
    cd django-resume-builder
    ```

2. **Create a Virtual Environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the Server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the Application:**

    Open your browser and go to `http://127.0.0.1:8000/`.

## Usage

1. **Create Resume:**

    Fill in the form with your personal information, education, experience, certifications, projects, and skills. Click "Save and View Resume" to generate the resume.

2. **View and Download Resume:**

    View your resume in a professional format. Click "Download as PDF" to download the resume as a PDF file.

## Project Structure

- `builder/`
  - `migrations/`
  - `templates/`
    - `builder/`
      - `index.html` - Form to enter resume details
      - `view_resume.html` - View and download the generated resume
  - `__init__.py`
  - `admin.py`
  - `apps.py`
  - `forms.py` - Form for collecting resume details
  - `models.py` - Database models for storing resume details
  - `tests.py`
  - `views.py` - Views for handling requests and rendering templates
- `resume_builder/`
  - `__init__.py`
  - `settings.py`
  - `urls.py` - URL configuration
  - `wsgi.py`
  - `asgi.py`
- `manage.py` - Django management script
- `requirements.txt` - List of dependencies


## Acknowledgements

- [Django](https://www.djangoproject.com/) - The web framework used
- [WeasyPrint](https://weasyprint.org/) - For generating PDF files
- [Bootstrap](https://getbootstrap.com/) - For styling the templates

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your improvements.

## Contact

For any inquiries or feedback, feel free to contact:

- Name: Bicky 
- Email: bickykumarrai1@gmail.com
- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/bickys/)

