# Twitter_Backend
It is a backend created in Django(Python) for a twitter like application. It also includes the minimal frontend that is required to check its working.
The basic functionality for registration using unique usernames and the login in their account is implemented. It all maintains sessions for logging into the account.
It provides some extended functionalities like following/unfollowing the other users on the app; creating, reading and deleting tweets/posts from the homepage of the user.


## Getting Started
You can either download it or clone it from https://github.com/pjvj/Twitter_Backend.git in a new folder(say TwitterBackend) at some location in your PC.

### Prerequisites
From terminal/command prompt, change your present working directory to TwitterBackend(the folder in which you have downloaded this project).
The name of the project is TwitterBackend and the name of the app inside it is api.
Inside this folder, execute the following commands
```bash
# Activate the virtualenv to isolate our package dependencies locally
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install Django, Django REST framework, flask into the virtualenv
pip install django
pip install djangorestframework
pip install flask
```
Now sync your database for the first time:
```bash
python manage.py makemigrations
python manage.py migrate
```
You will see a db.sqlite file created in the TwitterBackend folder and a xxxx_initial.py in TwitterBackend/api/migrations.

## The templates
The templates are just there as examples for how your templates could look like, but they work excellent as well.
Some of the templates are: base.html , register.html , login.html , homepage.html , logout.html

## Documentation
Comments are provided in the code to highlight the functionality they perform.
### Some important files to understand
* TwitterBackend/api/models.py contains the schema of the database formed
* TwitterBackend/api/urls.py contains the url patterns to reach the desired page
* TwitterBackend/api/views.py contains all the functions that responds to the requests from the frontend
* TwitterBackend/api/forms.py contains forms/form formats for registration, login or others
* TwitterBackend/settings.py contains the necessary settings for the functioning of the backend. It does not require any more alterations for the current functionality to work
## Running the server
```bash
python manage.py runserver
```
In the web browser, open the localhost followed by any of the url patterns mentioned in TwitterBackend/api/urls.py to start using it.
