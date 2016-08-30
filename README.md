# Django App
Django App

(We should document the directory structure)


## Required python packages
Create an virtual environment and make sure your into that environment.
```
sudo pip3 install virtualenv
virtualenv venv
```
no you created a directory with a virtual environment in it. To activate the enviroment use the command:
```
source venv/bin/activate
```

To download the pypy packages use following command
```
pip install -r requirements.txt
```

If you add new packages use (Make sure your in the right directory or provide a path)
```
pip freeze > requirements.txt

```


## Initial data
If you want to fill the database with the initial data execute the following command on the JSON objects in fixtures.
Make sure you have updated your database with "python3 manage.py migrate"
```
python3 manage loaddata fixtures/sector.json
```
