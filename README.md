# Django Lender

[![Build Status](https://travis-ci.org/codefellows/django-lender-401d7.svg?branch=master)](https://travis-ci.org/codefellows/django-lender-401d7)

[![Coverage Status](https://coveralls.io/repos/github/codefellows/django-lender-401d7/badge.svg?branch=master)](https://coveralls.io/github/codefellows/django-lender-401d7?branch=master)

**Author:** Nicholas Hunt-Walker and the class of Python 401d5

An app for managing the lending of books from an online book library.

## Getting Started

Clone this repository into whatever directory you want to work from.

```bash
$ git clone https://github.com/codefellows/django-lender-401d7.git
```

Assuming that you have access to Python 3 at the system level, start up a new virtual environment.

```bash
$ cd django-lender-401d7
$ python3 -m venv ENV
$ source ENV/bin/activate
```

Once your environment has been activated, navigate to the project root, `lending_library`, and apply the migrations for the app.

```bash
(ENV) $ cd lending_library
(ENV) $ ./manage.py migrate
```

Finally, run the server in order to server the app on `localhost`

```bash
(ENV) $ ./manage.py runserver
```

Django will typically serve on port 8000, unless you specify otherwise.
You can access the locally-served site at the address `http://localhost:8000`.

## Running Tests

Running tests for the `django_lender` is fairly straightforward.
Navigate to the same directory as the `manage.py` file and type:

```bash
(ENV) $ coverage run manage.py test
```

This will show you which tests have failed, which tests have passed.
If you'd like a report of the actual coverage of your tests, type

```bash
(ENV) $ coverage report
```

This will read from the included `.coverage` file, with configuration set in the `.coveragerc` file.
Currently the configuration will show which lines were missing from the test coverage.

## Current Models (outside of Django built-ins)

*LenderProfile*

- user: one-to-one relationship with the User model
- location: a text field for a user's location



## Current URL Routes

- `/admin`
