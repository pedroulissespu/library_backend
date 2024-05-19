# Library API

## Requirements

- Docker
- Docker Compose

## Installation

1. Clone the repository:
    ```sh
   git clone https://github.com/pedroulissespu/library_backend
   cd config
   ```

2. Build and start the Docker containers:
    ```sh
   docker-compose up --build
   ```

3. Apply migrations:
    ```sh
   docker-compose exec web python manage.py migrate
   ```

4. Load initial data fixtures:
    ```sh
    docker-compose exec web python manage.py loaddata apps/books/fixtures/initial_data.json
    ```
   
5. Access the application:
    - API: `http://localhost:8000/api/`
    - Swagger: `http://localhost:8000/swagger/`

## Running Tests

1. Run the tests:
    ```sh
    docker-compose exec web python manage.py test
    ```

## API Endpoints

- `GET /api/books/`
- `POST /api/books/`
- `GET /api/books/<id>/`
- `PUT /api/books/<id>/`
- `PATCH /api/books/<id>/`
- `DELETE /api/books/<id>/`

- `GET /api/authors/`
- `POST /api/authors/`
- `GET /api/authors/<id>/`
- `PUT /api/authors/<id>/`
- `PATCH /api/authors/<id>/`
- `DELETE /api/authors/<id>/`

## Authentication

- Obtain Token: `POST /api/token/`
- Refresh Token: `POST /api/token/refresh/`
- Verify Token: `POST /api/token/verify/`
