# Home Care Platform

This is a Flight booking platform using the Django(python) featuring GraphQL. Some main features include:
- User Authentication
- Flight Booking
- Flight Search
- Flight Details
- Flight Booking History
- Flight Cancellation
- Add, Update, delete Flights (for admins)
- Add, Update, delete Airlines (for admins)
- Role based access control

Future Milestones: 
- add a frontend for the platform
- add a payment gateway
- add a chatbot for customer support
- add invoice templates
- support for dynamic pricing
- support for dynamic discounts

## Getting Started
Taking the very first step, you would be needed to clone repository using git:

```bash
git clone git@github.com:grvsh02/flight-booking-platform.git
```

A standard `requirements.txt` file has been provided, which contains all python dependencies required to run the platform:

```bash
pip install -r requirements.txt
```

Along with it is a `sample.env` file, which names all supported environment variables. You are expected to make `.env` file with your own actual values, including all required variables.
To build virtual environment for the directory:

```bash
python -m venv env
```

The last step is activating vitual environment, run the command below
```bash
env/scripts/activate
```

To begin with, first we must consider creating a db in our `PostgreSQL` by running:

```bash
sudo su - postgres
psql
CREATE DATABASE myproject;
CREATE USER myprojectuser WITH PASSWORD 'password';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8'
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
\q
exit
```

To get started with the backend, you would need to also have a `PostgreSQL` database running. The database parameters then need to be specified in your `.env` file.

When using the platform for the first time, you need to initialize the database by running the following commands:

```bash
python manage.py migrate
python manage.py createsuperuser
```

You would need to run `migrate` command everytime there is a change in the database schema. Which you can spot by seeing a new file in the `migrations` folder in any of the sub-apps.

After you make changes to the database schema (models.py), you need to run `makemigrations` to create the migration file, which needs to be committed with your changes.
This migration file is then used by everyone to apply the changes to their database by the `migrate` command.

To finally run your development server, use:

```bash
python manage.py runserver
```

Which will start your application at `http://localhost:8000/`.

## Contributors

This development/educational scenario was coded and created by:

- [@Gaurav Sharma](https://www.github.com/grvsh02)

## Documentation

- [Django](https://docs.djangoproject.com/en/4.1/)
- [PostgreSQL](https://www.postgresql.org/docs/)
- [Strawberry](https://strawberry.rocks/docs)