import pytest
from unittest.mock import Mock
from atividades.src.atividade14_email_service import EventHandler

def test_handle_event():
    email_service_mock = Mock()
    event_handler = EventHandler(email_service_mock)
    
    event = {'id': 1, 'name': 'Test Event'}
    event_handler.handle_event(event)
    
    email_service_mock.send_email.assert_called_once_with('test@example.com', 'Event Occurred', str(event))
