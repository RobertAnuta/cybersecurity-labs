# Running the Application

## Requirements

- Python 3.10 or newer
- pip

## Setup

1. Navigate to the `app/` folder.

```
cd app
```

2. Create and activate a virtual environment.

```
python -m venv venv
source venv/bin/activate
```

On Windows, activate with `venv\Scripts\activate` instead.

3. Install dependencies.

```
pip install -r requirements.txt
```

4. Create the database and seed it with a test user and the first training module.

```
python seed_db.py
```

This creates a `training.db` SQLite file in the `app/` folder and prints the test login credentials to the terminal.

5. Run the application.

```
python app.py
```

6. Open the app in a browser.

```
http://127.0.0.1:5000/login
```

## Test Login

```
Username: testuser
Password: Test1234
```

## Notes

- The database file (`training.db`) is created locally and is not committed to the repository.
*- `SECRET_KEY` in `app.py` is a placeholder value for local development only and should never be reused in a real deployment.*
