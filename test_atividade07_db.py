import pytest
from atividades.src.atividade07_db import User, Database, UserService

def test_create_user():
    user = User(name="John", email="john@email.com")
    assert user.name == "John" and user.email == "john@email.com"

def test_save_user():
    user = User(name="John", email="john@email.com")
    db = Database()
    user_service = UserService(db)
    assert user_service.save_user(user) == None

def test_save_user_without_name():
    user = User(name="", email="john@email.com")
    db = Database()
    user_service = UserService(db)

    with pytest.raises(ValueError) as excinfo:
        user_service.save_user(user)
    assert str(excinfo.value) == "User must have a name and email"

def test_save_user_without_email():
    user = User(name="John", email="")
    db = Database()
    user_service = UserService(db)

    with pytest.raises(ValueError) as excinfo:
        user_service.save_user(user)
    assert str(excinfo.value) == "User must have a name and email"
