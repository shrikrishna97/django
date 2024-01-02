
---

# Setting Up Django Project

## Step 1: Create a Django Project Directory

```bash
mkdir django
cd django/
```

## Step 2: Create a Virtual Environment

```bash
python3 -m venv env
source env/bin/activate
```

## Step 3: Install Django

```bash
pip3 install django
```

## Step 4: Create a Django Project

```bash
django-admin startproject myapp
```

## Step 5: Navigate to Project Directory

```bash
cd myapp/
```

## Step 6: Run the Django Development Server

```bash
python3 manage.py runserver
```

## Step 7: Open Project in Visual Studio Code

```bash
code .
```

---

Now, you have a Django project set up with a virtual environment. You can start the development server using `python3 manage.py runserver` and open the project in Visual Studio Code for further development.

Note: Ensure that you activate the virtual environment (`source env/bin/activate`) before running Django commands to ensure the project uses the correct dependencies.

--- 

You can save this document in a file with a ".md" extension (e.g., "django_setup.md") for easy readability using Markdown formatting.