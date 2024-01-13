### Authentic Python app

- A simple authentication micro-service built in Python and Flask

### Run the application in production mode

> uwsgi --socket 0.0.0.0:3200 --protocol=http -w wsgi:application