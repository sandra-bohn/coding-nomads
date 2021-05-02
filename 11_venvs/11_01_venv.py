'''
In your CodingNomads folder create a new folder. Inside of that folder:

1. Create a new virtual environment
python3 -m venv first_env
2. Activate the virtual environment
source first_env/bin/activate
3. Install at least 3 packages in the virtual environment.
pip install django
pip install numpy
pip install six
4. Freeze the installed packages to a requirements.txt file.
pip freeze > requirements.txt
5. Deactivate the virtual environment.
deactivate
6. Delete the virtual environment.
rm -fr first_env
7. Create a new virtual environment and install the packages from the requirements.txt file.
python3 -m venv second_env
source second_env/bin/activate
pip install -r requirements.txt
'''