# FindMyWorks Portal
Find my work portal.
___
### List of features:
1. User can create accounts.
2. User can create resume.
3. User can create project for showing.

## Setup Process
> ❗Make sure You have python 3.9 and pip installed on your machine.

### Step 1

1. Create a folder where you want to clone the project.
   - I am creating a folder named ‘example’ in desktop

2. Now navigate to "example" via cmd or terminal

(Linux)

```bash
cd desktop/example
```

### Step 2

> It️ *Optional but better to use a virtual environment for every project.*

If you don’t have any virtual environment manager installed in your machine.


1. Now clone the project and navigate to newsfeed-portal

```bash
git clone https://github.com/rakibulislam01/findmyworks.git
cd findmyworks
```

1. Install all the dependencies for the project.


```bash
pip install -r requirements.txt
```

1. Create a .env file in the project directory and copy from .env.example.

2. Crate a database with user:

```
CREATE DATABASE findmyworks;
CREATE USER findmyworks WITH PASSWORD 'findmyworks';
ALTER ROLE findmyworks SET client_encoding TO 'utf8';
ALTER ROLE findmyworks SET default_transaction_isolation TO 'read committed';
ALTER ROLE findmyworks SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE findmyworks TO findmyworks;
```

1. You are all setup, let’s migrate now.

```bash
python manage.py makemigrations
python manage.py migrate
```

1. Create a superuser to rule the site 😎 [email user]

```bash
python manage.py createsuperuser

```

> *follow the instructions*

1. Hahh! Long wait. Let’s visit the site now

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and rock 🤘
After all okay, Then you need to registration for new user. Then login and update
user setting for getting news.
