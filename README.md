# Backend Main
This is an API that contains the main functions. This will be forked into our main backend project.

## Repository Structure
Here is the overview of the repository's structure.
```
.
├── _main
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitignore
├── LICENSE
├── manage.py
├── README.md
├── requirement.txt
└── <your-apps-directory>
```

## Getting Started
### 1. Create Virtual Environment
Let's start this learn by creating your virtual environment (venv). Please refer to this link to see how to make it: https://gist.github.com/ryumada/c22133988fd1c22a66e4ed1b23eca233

### 2. Install The Packages in `requirement.txt`
```bash
pip install -r requirement.txt
```

### 3. Start The Development by Creating a New App
```bash
django-admin startapp app-name
```

### 4. Register the Packages and the Applications
Register the package you want to use and the application you've created on `settings.py` inside the `_main` directory. Then find the `INSTALLED_APPS` variable and insert the package name as the value.

### 5. Migrate the Database
```bash
python3 manage.py migrate
```

### 6. Create a New Initial User
```bash
python3 manage.py createsuperuser --email admin@example.com --username admin
```

### 7. Formatting your code using autopep8
This is used to follow pep 8 coding standards.
```bash
autopep8 --recursive --in-place --aggressive tokens
```
