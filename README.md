## About

- v-notification is a` Notification` micro-service, 
it uses [django-notifyAll](https://github.com/inforian/django-notifyAll)
library for sending notifications.


## Prerequisites

#### Environment Variables : 

 - DATABASE_NAME_NOTIFY
 - DATABASE_USER
 - DATABASE_PASSWORD
 - DATABASE_HOST
 - DATABASE_PORT
 - SECRET_KEY

 

## Installation :

1 ) Clone this repo

2 ) Setup virtual environment
```
cd <path-to-repo>/v-notification/

virtualenv -p /usr/bin/python3 env

```

3 ) Activate Virtual environment
```
source env/bin/activate
```
4 ) Install requirements

- Base Requirements

```
pip install -r requirements/base.txt

```
- Testing Requirements
```
pip install -r requirements/test.txt

```
- Local requirements
```
pip install -r requirements/local.txt

```
- Production requirements

```
pip install -r requirements/production.txt

```
5 ) Prerequisites
- Makes sure above `Prerequisites` we mentioned above must be defined and fulfilled.

6 ) Run Server 
```
python manage.py runserver
```

## API Reference : 

- API documentation is hosted on [Swagger hub](https://app.swaggerhub.com/apis/verisadmin/v-user/0.1) 
and is public.

 
## Tests : 

- You may need to specify `providers` test credentials in Test cases in order to
test respective notification, otherwise test case will run with fake credentials.

- Run tests using 
```
make test
```
 
 