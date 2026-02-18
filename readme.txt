# Python Testing Project

A Python project demonstrating unit testing with pytest, featuring user management and database functionality.

## Project Structure

```
Python Testing/
├── db.py           # Database class for user management
├── main.py         # UserManager class
├── test_db.py      # Tests for Database class
└── test_main.py    # Tests for UserManager class
```

## Features

- **Database**: In-memory user database with add, get, and delete operations
- **UserManager**: User management system with email storage
- **Comprehensive Tests**: Full test coverage using pytest fixtures

## Requirements

- Python 3.x
- pytest


## Running Tests

Run all tests:
```bash
pytest
```

Run specific test file:
```bash
pytest test_db.py
pytest test_main.py
```

Run with verbose output:
```bash
pytest -v
```


## Testing Features

- Pytest fixtures for clean test isolation
- Exception testing with pytest.raises
- Automatic cleanup after tests
- Duplicate user validation
- Error handling tests
