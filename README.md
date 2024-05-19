# Library API

## Requirements

- Docker
- Docker Compose
- Python 3.12
- Pyenv

## Python Installation

### For Windows : https://www.python.org/downloads/
### For Linux Systems : 
#### Ubuntu/Debian : 
   ```sh
   sudo apt install python3
   ```
#### CentOS / RHEL : 
   ```sh
   sudo yum install python3
   ```

#### CentOS / RHEL with DNF: 
   ```sh
   sudo dnf install python3
   ```

#### Fedora : 
   ```sh
   sudo dnf install python3
   ```

#### openSUSE : 
   ```sh
   sudo zypper install python3
   ```

#### Arch Linux : 
   ```sh
   sudo pacman -S  python3
   ```

#### Alpine Linux : 
   ```sh
   apk add python3
   ```

### For macOS :
   1. Open Terminal;
   2. Run the following command to install Homebrew if it is not already installed:
   ```sh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   3. After installing Homebrew, you can install Python with the following command:
   ```sh
   brew install python
   ```

## Pyenv Installation
To install Pyenv and its dependencies, I will leave the installation link for the dependencies and pyenv respectively:
1. https://github.com/pyenv/pyenv/wiki#suggested-build-environment
2. https://github.com/pyenv/pyenv?tab=readme-ov-file#getting-pyenv

## Configuring Pyenv and Setting up pre-commit locally
```shell
pyenv install 3.12.0
pyenv virtualenv 3.12.0 library_api
pyenv activate library_api

pip install -r requirements/base.txt
pre-commit install --allow-missing-config
```

## Installation

1. Clone the repository:
    ```sh
   git clone https://github.com/pedroulissespu/library_backend
   cd library_backend
   ```

2. Build and start the Docker containers:
    ```sh
   ./utility/build_docker.sh
   ```
   
To stop the container, just issue the following command:
   ```sh
   ./utility/stop_docker.sh
   ```

3. Make migrations and apply:
    ```sh
   ./utility/migrations_docker.sh
   ```
   
4. Load initial data fixtures:
    ```sh
    ./utility/load_data.sh
    ```
   
5. Create Super User:
   ```sh
   ./utility/createsuperuser.sh
   ```

6. Access the application:
    - API: `http://0.0.0.0:8000/api/v1/`
    - Swagger: `http://0.0.0.0:8000/api/v1/docs/`

## Running Tests

1. Run the tests:
    ```sh
    ./utility/test.sh
    ```

## API Endpoints

- `GET /api/v1/books/`
- `POST /api/v1/books/`
- `GET /api/v1/books/<id>/`
- `PUT /api/v1/books/<id>/`
- `PATCH /api/v1/books/<id>/`
- `DELETE /api/v1/books/<id>/`

- `GET /api/v1/authors/`
- `POST /api/v1/authors/`
- `GET /api/v1/authors/<id>/`
- `PUT /api/v1/authors/<id>/`
- `PATCH /api/v1/authors/<id>/`
- `DELETE /api/v1/authors/<id>/`

## Authentication

- Obtain Token: `POST /api/v1/token/`
- Refresh Token: `POST /api/v1/token/refresh/`
- Verify Token: `POST /api/v1/token/verify/`
