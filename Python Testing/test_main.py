# from main import get_weather
# from main import add, divide
from main import UserManager
import pytest

# def test_get_weather():
#     assert get_weather(30) == "Hot"
#     assert get_weather(16) == "Warm"
#     assert get_weather(10) == "Cold"
    
# def test_add():
#     assert add(2,3) == 5, "2 + 3 should be 5"
#     assert add(-1,1) == 0, "-1 + 1 should be 0"
#     assert add(0,0) == 0, "0 + 0 should be 0"

# def test_divide():
#     with pytest.raises(ValueError, match="Cannot divide by zero"):
#         divide(10, 0)

@pytest.fixture
def user_manager():
    """ Creates a fresh instance of UserManager before each test."""
    return UserManager()

def test_add_user(user_manager):
    assert user_manager.add_user("john_doe", "john@example.com")==True
    assert user_manager.get_user("john_doe") == "john@example.com"


def test_add_user_duplicate(user_manager):
    user_manager.add_user("john_doe", "john@example.com")
    with pytest.raises(ValueError, match="User already exists"):
        user_manager.add_user("john_doe", "john2@example.com")

