## Django's MVT Architechture:

In Django’s own terminology, it follows the **Model-View-Template (MVT)** pattern, which is a variation of MVC. Here's how views in Django correspond to controllers in MVC:

### MVT (Django) vs MVC (Other Frameworks):

- **Model**: Represents the data structure, typically tied to a database table.
- **View (Django's View)**: Handles the logic and control flow, responding to requests and returning the response. This is similar to the **Controller** in traditional MVC frameworks.
- **Template**: Handles the presentation, which in MVC would typically be managed by the **View**.

### So, in essence:
Django’s **views** act as **controllers** in the **MVC** model because they:
1. **Receive input** (via HTTP requests),
2. **Process that input** (often involving interactions with models to fetch or update data),
3. **Return a response** (usually by rendering a template or sending data back).


### In Summary:
- **Django’s View**: Is more akin to the **Controller** in MVC.
- **Django’s Template**: Handles the presentation part, which would typically be the **View** in MVC.
- **Django’s Model**: Directly aligns with the **Model** in MVC.

To summarize, while Django uses the term "View," functionally, it behaves similarly to a **Controller** in the traditional **MVC** pattern. However, Django developers still use "views" to refer to the code that handles requests and returns responses, distinguishing it from the "view" part of MVC, which refers to the user interface.

<br>

---

<br>

## How Django App works
![image](https://photos.fife.usercontent.google.com/pw/AP1GczMcy0ehbxiKbnGUtvHZdsz9Qp2dkJVdSF-jBTqZI-V6vuwYhTnkhuU=w512-h384-s-no-gm?authuser=0)

### Step-by-Step Breakdown

**User Request:**

The user initiates the process by making a request to the Django application via a browser or other client. This request is in the form of a URL.

**URL Resolution:**

The Django URL resolution system takes over. It matches the URL in the request with URL patterns defined in the `urls.py` file. This file acts as a routing mechanism, directing the request to the appropriate view function.

**View Function:**

The view function, typically defined in a `views.py` file, handles the incoming request. It can:
- Process the request data.
- Interact with the database to fetch or modify data using Django's ORM (Object-Relational Mapper).
- Perform any necessary calculations or logic.
- Render a template to create the HTML response.

**Template Rendering (Optional):**

If the view function requires rendering a template, it uses Django's template engine to generate HTML content. Templates are essentially HTML files with placeholders that can be filled with dynamic data from the view function.

**Response:**

The view function returns a response to the user. This response can be:
- An HTML page generated from a template.
- A JSON or XML data structure.
- A redirect to another URL.
- A simple text message.

**In short**

- **Django**: The core framework that orchestrates the entire process.
- **URL Resolver**: Component responsible for matching incoming URL requests to the appropriate view function. It looks at the URL pattern defined in the urls.py file and determines which view should handle the request. If a match is found, the resolver passes control to the corresponding view function.
- **URLs.py**: File containing URL patterns.
- **Views.py**: File containing view functions.
- **Models.py**: File defining database models.
- **DB**: Database where data is stored and retrieved.

---

## Loading and Configuring(settings.py) Static files and templates
<br>

### Loading Templates
In Django, the TEMPLATES setting specifies how templates are managed.

- **DIRS:** This is a list of directories where Django looks for templates. In your example, it’s set to ['templates'], which means Django will look for templates inside a folder named templates at the root of your project.

- **APP_DIRS:** When set to True, Django will also look for templates inside a templates folder within each app.

When you use return render(request, 'index.html') in the home view, Django searches for index.html:

1. First, it looks in the templates directory you specified in DIRS.
2. f APP_DIRS is True, it also looks in the templates folder inside each app.   


So, to make sure index.html is found, you need to place it inside a folder named templates in the root directory of your project or inside the templates directory of a specific app.

<br>

### Loading Static Files

**{% load static %}:** This tag enables the use of the {% static %} template tag in the HTML file, which resolves the URL for static files.
**<link rel="stylesheet" href="{% static 'style.css' %}">:** This includes the style.css file from the static directory in your project.

```python
my_project/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
├── templates/
│   └── index.html
└── settingUpProject/
    ├── settings.py
    ├── urls.py
    └── ...

```
If style.css is located in the static/css folder:

```python
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```
#### Django Settings for Static Files

1. BASE_DIR:

**Definition:** The base directory of your project where the manage.py file is located.
**Purpose:** Used to build paths for other directories like static, templates, and media.

```python
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
```

Output:
```python
C:\Users\SaimNomani\Desktop\settingUpProject
```

2. STATIC_URL:

**Definition:** The URL prefix to access static files.

```python
STATIC_URL = 'static/'  # Maps to /static/ in the browser.
```

If you visit /static/css/style.css, Django will serve the file.

3. **STATICFILES_DIRS:**

**Definition:** A list of directories where Django will search for additional static files.

```python
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

Django will look for static files in the static/ folder at the base directory.

---

# Understanding `STATIC_URL` and `STATICFILES_DIRS` in Django

### **What is `STATIC_URL`?**
- **Purpose**: `STATIC_URL` defines the **URL path** that Django uses to serve static files (like CSS, JavaScript, and images) to the browser.
- Without it, Django wouldn’t know how to generate URLs to serve your static files.

---

### **What is `STATICFILES_DIRS`?**
- **Purpose**: `STATICFILES_DIRS` is a list of **file system paths** where Django looks for static files in addition to app-level static folders.
- Without it, Django wouldn’t know where to look for static files on your filesystem.

---

### **Why Are Both Needed?**
1. **`STATICFILES_DIRS`**:
   - Specifies the actual **location of static files** on your filesystem.
   - Example: It points Django to your project's `static` folder.

2. **`STATIC_URL`**:
   - Specifies the **URL prefix** browsers will use to access these static files.
   - Example: It tells browsers to look for files under `/static/`.

Together, they link your local static file storage with web access.

---

### **How They Work Together**
1. **`STATICFILES_DIRS`** tells Django **where to find static files** in your project.
2. **`STATIC_URL`** defines **how browsers access these files** via a URL.

---

### **Code Example**
#### **Django `settings.py`:**
```python
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = 'static/'  # URL prefix for static files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Directory for static files
```


### What Happens Behind the Scenes
**STATICFILES_DIRS:**

Django looks for style.css in the static/css folder.


**STATIC_URL:**

- When {% static 'css/style.css' %} is used in the template, Django generates the URL:

```python
/static/css/style.css
```

**Browser:**

- The browser requests /static/css/style.css and Django serves the file.


### What Happens in Production?
- During production, Django uses the collectstatic command to gather all static files into a single folder (e.g., /var/www/static/).
- STATIC_URL then maps this folder to /static/ so a web server (like Nginx or Apache) can serve the files.