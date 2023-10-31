import subprocess
import os


# Check if virtualenvwrapper is installed
if subprocess.call(['which', 'virtualenvwrapper']) == 1:
    subprocess.call(['pip', "install", "virtualenvwrapper"])
   # virtualenvwrapper is installed, create a new virtual environment
if subprocess.call(['which', 'virtualenvwrapper']) == 0:
    venv_name = "{{ cookiecutter.project_name }}"
    subprocess.call(['mkvirtualenv', venv_name])
    subprocess.call(['setvirtualenvproject'])

# Update poetry to the latest version
subprocess.call(['poetry', 'self', 'update'])
subprocess.call(['make', 'init-dev'])
