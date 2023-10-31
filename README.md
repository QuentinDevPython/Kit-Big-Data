# TaskTracker

## Collaboration

This project is the result of the collaboration between two AI engineers, students in the Specialized Mystery program at Telecom Paris: Reda Chenna @vulca1n and Quentin Barthélémy @QuentinDevPython, as part of the "Big Data Kit" course.

:bulb: Project main idea

The main idea of the project is to implement a simple task tracker using Python while respecting the conventions and norms used in production code.

We created two versions : 
- One using the shell with the CLI
- Another one using a web app using the Django Framework

We also implemented loggers to keep track of user actions and a Sphinx documentation (in both versions).

<img src="https://github.com/QuentinDevPython/Kit-Big-Data/blob/dev/images/sphinx_doc.png" width="500" height="500" />

## To access the project

First of all, you have to clone the repository and access to the project:

```shell
git clone https://github.com/QuentinDevPython/Kit-Big-Data.git
cd Kit-Big-Data
```

## Shell version

### Setup

For the shell version, you only need to install the dependies in the requirements.txt file:

```shell
pip install -r requirements.txt
```

### Accessing the app

Once installed, you can access the dedicated package:

```shell
cd shell-version
```

### Features implemented

You can know manage your todo list by executing CLI commands in the shell.

All the information is saved in a JSON file and will be loaded for each command.

For each command, a menu will also be displayed, asking you for some necessary information to fill.

#### Add a task

```shell
python src/main.py add-task
```

#### Remove a task (by name or id)

```shell
python src/main.py rm-task
```

or

```shell
python src/main.py rm-task-id
```

#### Mark a task as completed (by name or id)

```shell
python src/main.py complete-task
```

or

```shell
python src/main.py complete-task-id
```

#### Set the percentage of completed task (by name or id)

```shell
python src/main.py set-completion-task
```

or

```shell
python src/main.py set-completion-task-id
```

#### Set the due date of the task (by name or id)

```shell
python src/main.py set-date-task  
```

or

```shell
python src/main.py set-date-task-id
```

#### Set the description of the task (by name or id)

```shell
python src/main.py set-description-task 
```

or

```shell
python src/main.py set-description-task-id
```

#### Display all the tasks

```shell
python src/main.py display-task
```

#### Display all the tasks in a TODO list

```shell
python src/main.py display-todo
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
cd django-version
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
