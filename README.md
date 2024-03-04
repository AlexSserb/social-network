# Social network

## Table of contents
* [Technologies](#technologies)
* [Tools](#tools)
* [Installation](#installation)

<a name="technologies"></a>
## Technologies
* Python 3.10
* Flask
* Flask-SQLAlchemy
* PostgreSQL
* Redis
* HTML, CSS, Jinja2

<a name="tools"></a>
## Tools
* Python interpreter
* PgAdmin 4
* Redis CLI
* VS Code
* Package manager for Python - pip
* Git


<a name="installation"></a>
## Installation
1. Clone the repository:
    ```commandline
    git clone https://github.com/AlexSserb/social-network.git
    ```
2. Create and configure the database.

    2.1. Ensure your PostgreSQL and Redis servers are running.

    2.2. In PostgreSQL, create a database with your user as the owner.

    2.3. Copy `.env.example` file as `.env` and update with the following fields with your database and app credentials:
    ```
    DATABASE_ADDRESS=
    DATABASE_NAME=
    DATABASE_PORT=
    DATABASE_USER=
    DATABASE_PASSWORD=

    SESSION_REDIS=

    SECRET_KEY=
    ```

3. Run the backend part.

    3.1. Create and activate virtual environment:
    ```commandline
    python -m venv venv 
    venv\\Scripts\\activate
    ```
    3.2. Install requirements:
    ```commandline
    pip install -r requirements.txt 
    ```
    3.3. Create migrations:
    ```commandline
    flask db init 
    flask db migrate
    flask db upgrade
    ```
    3.4. Start the backend server:
    ```commandline
    flask --app app run
    ```
