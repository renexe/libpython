from unittest.mock import Mock

from libpythonpro import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        "login": "renexe", "id": 9634767, "node_id": "MDQ6VXNlcjk2MzQ3Njc=",
        "avatar_url": "https://avatars1.githubusercontent.com/u/9634767?v=4"
    }
    github_api.requests.get = Mock(return_value = resp_mock)
    url = github_api.buscar_avatar('renexe')
    assert 'https://avatars1.githubusercontent.com/u/9634767?v=4' == url