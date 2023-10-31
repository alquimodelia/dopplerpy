import subprocess
import os

# setup venv
new_dir = "{{ cookiecutter.project_name }}"
os.chdir(new_dir)
print(subprocess.call(['which', 'virtualenvwrapper']))
# Check if virtualenvwrapper is installed
if subprocess.call(['which', 'virtualenvwrapper']) == 0:
   # virtualenvwrapper is installed, create a new virtual environment
   venv_name = "{{ cookiecutter.project_name }}_venv"
   subprocess.call(['mkvirtualenv', venv_name])
   subprocess.call(['setvirtualenvproject'])

# Update poetry to the latest version
subprocess.call(['poetry', 'self', 'update'])
subprocess.call(['make', 'init-dev'])
