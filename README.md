# TaskTracker

## Collaboration

This project is the result of the collaboration between two AI engineers, students in the Specialized Mystery program at Telecom Paris: Reda Chenna @vulca1n and Quentin Barthélémy @QuentinDevPython, as part of the "Big Data Kit" course.

:bulb: Project main idea

The main idea of the project is to implement a simple task tracker using Python while respecting the conventions and norms used in production code.

We created two versions : 
- One using the shell with the CLI
- Another one using a web app using the Django Framework

We also implemented loggers to keep track of user actions and a Sphinx documentation (in both versions).

<img src="https://github.com/QuentinDevPython/Kit-Big-Data/blob/dev/images/sphinx_doc.png" width="500" height="320" />

## To access the project

First of all, you have to clone the repository:

```shell
git clone https://github.com/QuentinDevPython/Kit-Big-Data.git
cd Kit-Big-Data
```

## Shell version

### Setup

```shell
pip install -r requirements.txt
```


## Django version

For Django, you need to install a few more dependencies.

### Setup

There are two ways to launch the app:

#### 1. Local

```shell
cd django-version/todo_list
pip install -r docker-setup.txt
```

Migrate databases:

```shell
python manage.py makemigrations
python manage.py migrate
```

To launch the server:

```shell
python manage.py runserver
```

#### 2. Docker

If you haven't downloaded Docker yet, please follow the steps through this link: https://docs.docker.com/engine/install/

Then, you can setup the needed Docker container by doing:

```shell
docker-compose up
```

### Accessing the app

When your server is running, you can connect to the ```localhost:8000``` on your browser.

### Features implemented

#### Login

<img src="https://github.com/QuentinDevPython/Kit-Big-Data/blob/dev/images/login_page.png" width="500" height="320" />

#### Tasklist

<img src="https://github.com/QuentinDevPython/Kit-Big-Data/blob/dev/images/task_page.png" width="500" height="320" />

#### Filter tasklist

<img src="https://github.com/QuentinDevPython/Kit-Big-Data/blob/dev/images/task_filter.png" width="500" height="320" />

#### Create task / Update task

<img src="https://github.com/QuentinDevPython/Kit-Big-Data/blob/dev/images/task_update.png" width="500" height="320" />

#### Delete task

<img src="https://github.com/QuentinDevPython/Kit-Big-Data/blob/dev/images/task_delete.png" width="500" height="320" />
