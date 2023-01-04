# Project : NameofProject

## Check The Live Website ➡️ [Live Website](https://projectdeploylink.github.io)

## Visualization of the Website

![Form](./project.gif)

## Description

Project aims to create an app using Django.

## Learning Outcomes

At the end of the project, you will be able to;

- improve coding skills within Python & Django & Rest-Framework.

- use git commands (push, pull, commit, add etc.) and Github as Version Control System.

## Problem Statement

- We are adding a new project to our portfolios. So you and your colleagues have started to work on the project.

## Project Skeleton

```
Project(folder)
|
|----README.md
├── env
│     └── index.html
├── main
│    ├── __init__.py
│    ├── asgi.py
│    ├── settings.py
│    ├── urls.py
│    ├── wsgi.py
├── appname
│    ├── __init__.py
│    ├── admin.py
│    ├── apps.py
│    ├── faker.py
│    ├── models.py
│    ├── permissions.py
│    ├── serializer.py
│    ├── test.py
│    ├── urls.py
│    ├── views.py
├── .env
├── .gitignore
├── db.sqlite3
├── manage.py
└── requirements.txt
```

### Requirements

- python --version
- pip --version
- python -m venv env
- source env/Scripts/Activate
- pip install django
- pip install --upgrade pip
- pip install pillow
- pip install python-decouple
- pip install djangorestframework
- pip install Faker
- pip install django-filter
- pip install django-cors-headers
- django-admin startproject main .
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver

### Overview

I mastered Python & Django & JS & Rest-Framework features in this project.
You can see the visual representation above.

## Notes

- Step 1: Create React App using `npx create-react-app project-name`

- Step 2: For images you can use [Images](./src/helper/data.js).

- Step 3: Push your application into your own public repo on Github

- Step 4: Add project gif to your project and README.md file.

## Resources

- 🔥 You can use [`data.js`](./src/helper/data.js) for your own work.

## Support

- Open an Issue, I will check it a soon as possible 👀

- Don't forget to show your support by ⭐ the project!!

## Quick start

- Clone this repo using git clone https://github.com/SkyCooper/NameofProject.git

- Move to the appropriate directory: cd recipe-app.

- Run npm run install in order to install dependencies and clean the git repo.

- Change configurations in /src/config/config.js according to your cosmicjs bucket.

- Run npm run dev to start the project in dev mode.

- Run npm run build to build the project in /dist folder.

- Now you're ready to rumble!

## Contributing

- Fork it (https://github.com/SkyCooper/NameofProject)

- Create your feature branch (git checkout -b feature/fooBar)

- Commit your changes (git commit -am 'Add some fooBar')

- Push to the branch (git push origin feature/fooBar)

- Create a new Pull Request

# <center> ⌛ Happy Coding ✍ </center>

//////////////////////--------------------------------////////////////////////

## Features :

- Create Bank Account.
- Deposit & Withdraw Money
- Bank Account Type Support (e.g. Current Account, Savings Account)
- Interest calculation depending on the Bank Account type
- Transaction report with a date range filter
- See balance after every transaction in the Transaction Report
- Calculate Monthly Interest Using Celery Scheduled tasks
- More efficient and accurate interest calculation and balance update
- Ability to add Minimum and Maximum Transaction amount restriction
- Modern UI with Tailwind CSS

## Prerequisites :

Be sure you have the following installed on your development machine:

- Python >= 3.7
- Redis Server
- Git
- pip
- Virtualenv (virtualenvwrapper is recommended)

## Requirements :

- celery==4.4.7
- Django==3.2
- django-celery-beat==2.0.0
- python-dateutil==2.8.1
- redis==3.5.3

## Django Installation Steps :

- Install Python 3.7 Or Higher
- Install Django version 2.2.0
- Install all dependencies cmd -python -m pip install –-user -r requirements.txt
- Finally run cmd - python manage.py runserver

admin email - admin@admin.com
admin password - admin123
