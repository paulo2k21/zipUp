import pytest
from unittest.mock import MagicMock
from atividades.src.atividade10_user_service import UserManager

user_service = MagicMock()
user_manager = UserManager(user_service)

def test_fetch_user_info_success():
    user_id = 1
    expected_user_info = {"user_id": 1, "name": "John"}

    user_service.get_user_info.return_value = expected_user_info

    user_info = user_manager.fetch_user_info(user_id)

    assert user_info == expected_user_info
    user_service.get_user_info.assert_called_once_with(user_id)

def test_fetch_user_info_user_not_found():
    user_id = 2
    user_service.get_user_info.return_value = None

    try:
        user_manager.fetch_user_info(user_id)
        assert False
    except ValueError as e:
        assert str(e) == "User not found"