# Book manager
Simple app to test POST request adding instances to two separate services. For local use only.

# Running
1. [Install Docker](https://docs.docker.com/get-docker/)
2. Run `docker-compose up` from project directory

# Workflow
1. Make request to http://localhost:8000/book/add_book/: `curl -d '{"title": "Crime and Punishment", "author": "Dostoevsky"}' -H 'Content-Type: application/json' -X POST http://localhost:8000/book/add_book/`
2. `Printer` service saves book to its own database.
3. `Printer` service sends Celery task to handle `Counter` service.
4. Celery task sends POST to `Counter` service. No authentication or CSRF handling for simplicity reasons.
5. `Counter` service adds Author to its database (if not present) and adds 1 to his/her book numbers. 

# Load testing
You can use [Locust](https://docs.locust.io/en/stable/quickstart.html) to load test services.
1. `pip install locust`
2. `locust -f locust.py`
