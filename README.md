# Steps for setup

## Installation

_create virtual environment_

```
virtualenv --python=python3.8 .env
```

Make sure project and virtual environment should be on same level

_Activate environment_

```
source .env/bin/activate
```

_Now change directory to project_

```
cd project_folder_name
```
_Before installing packages make sure your pip is up to date install it by_ or [follow this link](https://pip.pypa.io/en/stable/installing/)
```
pip install --upgrade pip
```
_Time to install dependencies (It will take a while)_
```
pip install -r requirements.txt
```

_Create table in database_
```
python manage.py migrate
```

### Install and run Redis Server for Celery(Using for asynchronously saving the Holiday details on user Sign-up)

_Run Redis Server_

```
redis-server
```

_If want to check celery asynchronous function logs_

```
celery -A social_networking_project worker -l INFO
```

### API Endpoints

_To get jwt acess and refresh token for calling it from third party application(like postman)_

```
http://localhost:8000/api/token/
```

_To get jwt acess from refresh token_

```
http://localhost:8000/api/token/refresh/
```

API Endpoint | Parameter | Request Type | Purpose | Output 
------------ | ------------- | ------------- | ------------- | -------------
http://localhost:8000/api/token/ | pass vaild "username" and "password" in form-data | POST | Getting access token | Returns dict of "access" and "refresh token"
http://localhost:8000/api/token/refresh/ | pass "refresh" token in form-data | POST | Getting access token from refresh token if expired | Returns "access" token
http://localhost:8000/rest/user/ | pass "access" token in request headers(i.e "Bearer your_access_token") | POST | user sign-up | Returns created user data
http://localhost:8000/rest/post/ | pass "access" token in request headers(i.e "Bearer your_access_token") | GET | Blogs/Posts list | Returns all the available blogs list
http://localhost:8000/rest/post/ | pass "access" token in request headers(i.e "Bearer your_access_token") + blog data(i.e name and description) in form-data | POST | Create new Blog | -
http://localhost:8000/rest/post/likes | pass "access" token in request headers(i.e "Bearer your_access_token") + data(i.e user_id = current_user_ID, like_status = "like" or "unlike" and blog_id = ID of blog on which user is reacting) in form-data | POST | Like/Dislike Blogs | -


### Test cases
_Run test cases_

```
python3 manage.py test social_networking_project.tests.test_views
```

### To start project

_To start server_
```
python manage.py runserver
```
_And navigate to below url in browser
```
http://127.0.0.1:8000/
```
