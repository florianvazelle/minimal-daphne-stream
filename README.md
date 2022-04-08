# Minimal Example 

## Setup

```
virtualenv --python 3.10 venv/
source venv/bin/activate
pip install Django==3.2.12 daphne==3.0.2
```

### Reproduce the stream issue

Run the django app with:
```
daphne myproject.asgi:application
```

In another terminal, run:
```
curl http://localhost:8000/stream/
```


### Reproduce what I expected to happen

Run the django app with:
```
python manage.py runserver
```

In another terminal, run:
```
curl http://localhost:8000/stream/
```