## UV Package Manager
The uv package on PyPI is a Python library for managing and working with package dependencies. It appears to focus on simplifying dependency management, particularly for workflows involving tools like Poetry.

### Common Commands:
1. **install uv:** 
```python
pip install uv
```

2. **Creating vitual environment:** 
```python
uv venv // create vitial environment at .venv folder.
```

3. **activate vitual environment:** 
```python
.venv/scripts/activate
```

4. **install package:** 
```python
uv pip install Django
```

5. **To create Django project:** 
```python
django-admin startproject [projectname]
```

6. **To run server:** 
```python
python manage.py(complete path where manage.py exist) runserver 8000(port optional)
```

## Typical Django Project File Structure

```python
myproject/
│
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── myapp/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── urls.py
│
├── static/
│   └── css/
│   └── js/
│   └── images/
│
├── media/
├── templates/
│   ├── base.html
│   └── myapp/
│       └── index.html
├── db.sqlite3
├── requirements.txt
├── .gitignore
└── README.md

```

### 1. Project Root Directory:
At the root of the Django project, you will typically have the following structure:

```python
myproject/
├── manage.py
├── myproject/
├── db.sqlite3
├── requirements.txt
├── .gitignore
└── README.md
```
- **manage.py:** This file is used to manage the project and perform administrative tasks like running the server, database migrations, and creating new apps.
- **myproject/:** This directory is the project directory and contains the settings, URLs, and other configurations.
- **db.sqlite3:** This is the default SQLite database file, which stores data for your project.
- **requirements.txt:** This file contains the list of all the Python packages needed for your project. It’s used for creating a virtual environment or deploying the project.
- **.gitignore:** This file contains a list of files and directories that Git should ignore. It typically includes __pycache__, .env, and other generated files.
- **README.md:** A markdown file that usually contains an introduction, setup instructions, and other details about your project.
<br>

### 2. The Main Project Folder (myproject/):
Inside the main project directory (which shares the project’s name), you'll have the following files and folders:

```python
myproject/
├── __init__.py
├── settings.py
├── urls.py
├── asgi.py
└── wsgi.py
```

- __init__.py: This file makes Python treat the directory as a package. It’s typically empty but signals to Python that this directory should be treated as part of a Python module.
- settings.py: Contains all the settings and configurations for the project (e.g., database configuration, middleware, installed apps, etc.).
- **urls.py:** Contains URL routing information for the project, which maps requested URLs to the views.
- **asgi.py:** For asynchronous server communication. This file defines the ASGI application used for handling requests asynchronously.
- **wsgi.py:** The entry point for WSGI-compatible web servers (e.g., Gunicorn or uWSGI) to serve the project.

<br>

### 3. Apps Directory:
Django projects are divided into apps, which are self-contained modules with a specific purpose (e.g., a blog, a user authentication system). When you create a new app using python manage.py startapp <appname>, it generates the following 

```python
myapp/
├── migrations/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
└── urls.py
```

- **migrations/:** This folder stores migration files, which Django uses to keep track of changes to your database schema.
- **__init__.py:** This file is used to mark the directory as a Python package.
- **admin.py:** This file is used to register models to be displayed in the Django admin interface.
- **apps.py:** Contains configuration for the app (e.g., name and settings).
- **models.py:** Defines the data models (tables) for your app.
- **tests.py:** Contains test cases to ensure that your application behaves as expected.
- **views.py:** Contains the views that define the request-handling logic for your app.
- **urls.py:** Contains URL routing specific to the app, usually with app-specific views.

<br>

### 4. Static and Media Directories:
These directories store static files (CSS, JavaScript, images) and user-uploaded media files, respectively.

```python
static/
└── css/
└── js/
└── images/

media/
└── uploads/
```

- **static/:** Holds static files like CSS, JavaScript, and images that are served to clients.
- **media/:** Holds user-uploaded files, such as images or documents, depending on the application.

<br>

### 5. Templates Directory:
This directory stores the HTML templates for rendering the views in Django.

```python
templates/
├── base.html
└── app_name/
    └── template_file.html
```

- **templates/:** Contains HTML files used for rendering views. You might have subdirectories for each app to keep templates organized.
- **base.html:** A common template that other templates extend, commonly used to structure the overall look and feel of the website.
- **app_name/:** Directory where each app might store its own specific templates.

<br>

## 6. Other Common Files:
There are several other files you might encounter depending on the project:

- **manage.py:** The command-line utility for managing the project, such as running the server, applying migrations, and creating apps.
- **requirements.txt:** Lists all dependencies for the project.
- **Procfile:** Used for deployment to platforms like Heroku.
- **Dockerfile:** Used to create a Docker image for deploying the project in containers.