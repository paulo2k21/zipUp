from atividades.src.atividade16_build_automation import automation_build, StatusEnum, InstallationEnum
from unittest.mock import MagicMock
from unittest.mock import patch

def test_automation_build_no_robots():
    with patch('atividades.src.atividade16_build_automation.db_context') as mock_db_context:
        mock_session = MagicMock()
        mock_db_context.return_value.__enter__.return_value = mock_session
        
        mock_automation = MagicMock()
        mock_automation.id = 1
        mock_automation.name = 'Automação teste'
        mock_session.query.return_value.filter_by.return_value.first.return_value = mock_automation
        
        mock_session.query.return_value.filter_by.return_value.all.return_value = []
        
        result = automation_build(1)
        
        assert result == 'Automation Automação teste has no robots to execute.'

def test_automation_build_all_robots_installed():
    with patch('atividades.src.atividade16_build_automation.db_context') as mock_db_context, \
        patch('atividades.src.atividade16_build_automation.orchestration_create') as mock_orchestration_create:
        
        mock_session = MagicMock()
        mock_db_context.return_value.__enter__.return_value = mock_session
        
        mock_automation = MagicMock()
        mock_automation.id = 1
        mock_automation.name = 'Automação teste'
        mock_session.query.return_value.filter_by.return_value.first.return_value = mock_automation
        
        mock_robot = MagicMock()
        mock_robot.installed = InstallationEnum.INSTALLED
        mock_session.query.return_value.filter_by.return_value.all.return_value = [mock_robot]
        
        result = automation_build(1)
        
        assert mock_automation.status == StatusEnum.RUNNING
        
        mock_session.commit.assert_called_once()
        mock_orchestration_create.assert_called_once_with(1)
        
        assert result == 'Automation Automação teste builded successfully'

def test_automation_build_robots_not_installed():
    with patch('atividades.src.atividade16_build_automation.db_context') as mock_db_context, \
         patch('atividades.src.atividade16_build_automation.send_to_pack') as mock_send_to_pack, \
         patch('atividades.src.atividade16_build_automation.orchestration_create') as mock_orchestration_create, \
         patch('atividades.src.atividade16_build_automation.automation_build') as mock_automation_build:
        
        mock_session = MagicMock()
        mock_db_context.return_value.__enter__.return_value = mock_session
        
        mock_automation = MagicMock()
        mock_automation.id = 1
        mock_automation.name = 'Automação teste'
        mock_session.query.return_value.filter_by.return_value.first.return_value = mock_automation
        
        mock_robot1 = MagicMock()
        mock_robot1.installed = InstallationEnum.INSTALLED
        
        mock_robot2 = MagicMock()
        mock_robot2.installed = InstallationEnum.NOT_INSTALLED
        
        mock_session.query.return_value.filter_by.return_value.all.return_value = [mock_robot1, mock_robot2]
        
        result = automation_build(1)
        
        assert mock_automation.status == StatusEnum.RUNNING
        
        mock_session.commit.assert_called_once()
        mock_send_to_pack.assert_called_once_with(mock_robot2.id)
        mock_orchestration_create.assert_not_called()
        mock_automation_build.assert_called_once_with(automation_id=1)
        
        assert result == 'there is robots to install, building automation 1 again'