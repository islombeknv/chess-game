
## 1. Clone the Repository

First, clone your project repository from GitHub to your server.


```bash
  git clone https://github.com/islombeknv/chess-game.git
  cd chess-game
```

## 2. Set Up the Environment

Create a Virtual Environment

```bash
  python3 -m venv env
  source env/bin/activate

```

## 3. Install Dependencies

Install the required packages using pip.

```bash
  pip install -r requirements.txt
```

## 4. Set Up Database

Apply database migrations to set up your database schema.

```bash
  python manage.py migrate
```

## 5. Create a Superuser

Create a superuser for accessing the Django admin interface.

```bash
  python manage.py createsuperuser
```

## 6. Static Files
Collect Static Files
```bash
  python manage.py collectstatic
```

## 7. Run Tests
Execute the tests to ensure everything is functioning correctly.
```bash
  python manage.py test
```

## 8. Data Generation:s
Generate realistic chess game records.
```bash
  python manage.py generate_games [argument]