import pytest
from unittest import mock
from atividades.src.atividade15_aws_detect_text import detect_text_resource

@mock.patch('boto3.Session')
@mock.patch('builtins.open', new_callable=mock.mock_open, read_data=b'fake_image_data')
def test_detect_text_resource(mock_open, mock_session):

    fake_response = {
            "DetectedText": "REPUBLICA FEDERATIVA DO BRASIL",
            "Type": "LINE",
            "Id": 0,
            "Confidence": 98.51686096191406,
            "Geometry": {
                "BoundingBox": {
                    "Width": 0.32718953490257263,
                    "Height": 0.0437319315969944,
                    "Left": 0.09317709505558014,
                    "Top": 0.055079568177461624
                },
                "Polygon": [
                    {
                        "X": 0.09323225915431976,
                        "Y": 0.055079568177461624
                    },
                    {
                        "X": 0.4203666150569916,
                        "Y": 0.05886908248066902
                    },
                    {
                        "X": 0.42031145095825195,
                        "Y": 0.09881149977445602
                    },
                    {
                        "X": 0.09317709505558014,
                        "Y": 0.09502198547124863
                    }
                ]
            }
        }

    mock_client = mock_session.return_value.client.return_value
    mock_client.detect_text.return_value = fake_response

    response = detect_text_resource('fake_image_path')

    mock_session.assert_called_once_with(profile_name='default')
    mock_session.return_value.client.assert_called_once_with('rekognition')
    mock_client.detect_text.assert_called_once_with(Image={'Bytes': b'fake_image_data'})
    mock_open.assert_called_once_with('fake_image_path', 'rb')

    assert response == fake_response