# OC-P8
### OpenClassrooms - My 8th project for OC PythonPath

### Introduction

Python/Django Web application allowing to substitute safer food products from existing one.
PostgreSQL is used. Data come from OpenFoodFacts API.

[http://purbeurre-paris.herokuapp.com/](http://purbeurre-paris.herokuapp.com/ "Pur beurre") 

### Local setup

#### Setup code

Create a directory, for example

```
mkdir purbeurre_webapp
cd purbeurre_webapp
```

Clone Git repository

```
git clone https://github.com/damien-devpy/OC-P8
cd purbeurre
```

#### Setup virtual environment 

```
pipenv shell
```

Installing dependencies

```
pipenv install
```

Contributing

```
pipenv install --dev
```

#### Tests

Running tests

```
manage.py run --source="." -m pytest --driver Firefox (all tests)
manage.py run -m pytest users_app (run tests only for users_app)
```

Test coverage

```
coverage run --source="." -m pytest --driver Firefox
coverage report -m

```

#### Launching local server 

Simply run :

```
python manage.py runserver
```

You can also populate database with :

```
python manage.py loaddb [how much products you want]
```
