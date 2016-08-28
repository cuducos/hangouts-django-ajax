# Papo aberto: Django & AJAX

Source for a [Hangouts On Air about Django & AJAX](https://plus.google.com/events/cuq69oss8gjevd66av0coaklqns?authkey=COuxzN63uaz_hAE).

## Installing

1. With [Python](http://python.org) 3.5 and `pip` install the dependencies: `$ python -m pip install -r requirements.txt`
1. Set your environment variables or `.env` file (maybe copying `contrib/.env.sample` to `.env` and editing it according to your needs)
1. Run migrations: `$ python manage.py migrate`
1. Create a _super user_ for you: `$ python manage.py createsuperuser`
1. Run tests: `$ python manage.py test`
1. Run the server: `$ python manage.py runserver`

## Endpoints

### Browser navigation

If user is authenticated (use [Django Admin](http://localhost:8000/admin/)) it shows the form to make a new booking via AJAX (to be created during the Hangout).

* [`/bookings/`](http://localhost:8000/bookings/): list all bookings from the current month
* [`/bookings/<year>/<month>/`](http://localhost:8000/bookings/2016/12/) (e.g. `/bookings/2016/12/`): list all bookings from the current month  

### API

All endpoints requires authentication (use [Django Admin](http://localhost:8000/admin/)).

* `GET /api/bookings/`: list all bookings
* `POST /api/bookings/`: create new booking
