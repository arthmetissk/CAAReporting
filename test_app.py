import pytest

from app import app, generate_chat_answer, ALL_CAMPAIGNS_DIR, REPORTS, MONTHLY_SUMMARIES
from campaign_knowledge import answer_from_knowledge, AUGUST_CAMPAIGNS


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client


def _login(client):
    return client.post('/login', data={'username': 'caa', 'password': 'twinleaf1234'}, follow_redirects=False)


def test_login_and_dashboard_are_protected(client):
    response = client.get('/')
    assert response.status_code == 302
    assert response.headers['Location'].endswith('/login')

    response = _login(client)
    assert response.status_code == 302
    assert response.headers['Location'] == '/'


def test_dashboard_renders_store_and_metrics(client):
    _login(client)
    response = client.get('/')
    assert response.status_code == 200
    body = response.data
    assert b'Smokers Warehouse' in body
    assert b'Twinleaf' in body
    assert b'SW1' in body
    assert b'TXP' in body
    assert b'$100,279' in body
    assert b'Ask results' in body


def test_campaign_archive_is_available(client):
    assert ALL_CAMPAIGNS_DIR.is_dir()
    assert (ALL_CAMPAIGNS_DIR / '2026_August_CAA_Campaign_Summary.html').is_file()

    _login(client)
    for report in REPORTS:
        response = client.get(f"/support-report/{report['id']}")
        assert response.status_code == 200, report['id']

    for month in MONTHLY_SUMMARIES:
        response = client.get(f"/monthly-summary/{month['slug']}")
        assert response.status_code == 200, month['slug']


def test_summary_and_shared_report_routes(client):
    _login(client)
    assert client.get('/summary-report').status_code == 200
    shared = client.get('/shared-report/2026_August_41g_Vape_Loyalty_Campaign.html')
    assert shared.status_code == 200
    blocked = client.get('/shared-report/../app.py')
    assert blocked.status_code == 404


def test_chat_returns_metrics_and_recommendations(client):
    _login(client)
    response = client.post('/api/chat', json={'query': 'Summarize August results with metrics'})
    assert response.status_code == 200
    payload = response.get_json()
    assert '$100,279' in payload['answer'] or 'Vape' in payload['answer']
    assert payload['metrics']
    assert payload['recommendations']
    assert payload['campaigns']


def test_chat_answers_store_brand_questions():
    answer, campaigns, recs = answer_from_knowledge('Compare Twinleaf vs Smokers Warehouse')
    assert 'Smokers Warehouse' in answer
    assert 'Twinleaf' in answer
    assert campaigns
    assert recs

    answer2 = generate_chat_answer('How did vape do at SW1 and SW2?')
    assert '68' in answer2 or '$68' in answer2 or 'Vape' in answer2
    assert len(answer2.split()) < 160


def test_healthcheck_reports_archive(client):
    response = client.get('/api/healthcheck')
    assert response.status_code == 200
    payload = response.get_json()
    assert payload['status'] == 'ok'
    assert payload['archive_html_files'] >= 20
    assert len(AUGUST_CAMPAIGNS) == 4
