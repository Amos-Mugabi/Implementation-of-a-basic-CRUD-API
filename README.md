# backend
 
Implementation of CRUD API and Testing

Implementation of a basic CRUD API for one feature in the project. This involved developing the necessary models, serializers, and views using Django REST Framework. After implementing the API, tested it using Postman by making GET and POST requests to verify data retrieval and creation.

Challenges and Solutions

Challenge: Authentication errors when accessing protected endpoints.
Solution: Implemented Token Authentication using Django REST Framework and included the token in the request headers.

Challenge: Database migrations failing due to model changes.
Solution: Ran python manage.py makemigrations and python manage.py migrate to ensure database consistency.
