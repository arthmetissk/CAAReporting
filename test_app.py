import pytest
from app import app, generate_chat_answer

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client

def test_login_and_dashboard_are_protected(client):
    response = client.get('/')
    assert response.status_code == 302
    assert response.headers['Location'].endswith('/login')

    response = client.post('/login', data={'username': 'caa', 'password': 'twinleaf1234'}, follow_redirects=False)
    assert response.status_code == 302
    assert response.headers['Location'] == '/'


def test_chat_answer_is_concise_and_recommendation_focused(client):
    answer = generate_chat_answer('How should we improve loyalty and recommendations?')
    assert isinstance(answer, str)
    assert len(answer.split()) < 80
    assert 'recommend' in answer.lower() or 'prioritize' in answer.lower()
