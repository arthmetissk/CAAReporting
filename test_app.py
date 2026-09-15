import pytest

from app import app, generate_chat_answer, ALL_CAMPAIGNS_DIR, REPORTS, MONTHLY_SUMMARIES, ALL_CAMPAIGN_CARDS
from campaign_knowledge import answer_from_knowledge, CAMPAIGN_FAMILIES, MONTHLY_STORIES


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


def test_dashboard_renders_month_family_store_browse(client):
    _login(client)
    response = client.get('/')
    assert response.status_code == 200
    body = response.data
    assert b'By month' in body
    assert b'Continuous families' in body
    assert b'Breakfast + Free Coffee' in body
    assert b'Sandwich Deal' in body
    assert b'Fireworks Summer Program' in body
    assert b'May 2026' in body
    assert b'SW1' in body
    assert b'TGC' in body


def test_campaign_archive_is_available(client):
    assert ALL_CAMPAIGNS_DIR.is_dir()
    _login(client)
    for report in REPORTS:
        response = client.get(f"/support-report/{report['id']}")
        assert response.status_code == 200, report['id']
    # sample continuous family reports
    for cid in ['may-sandwich', 'june-fireworks', 'july-breakfast-coffee']:
        assert client.get(f'/support-report/{cid}').status_code == 200, cid
    for month in MONTHLY_SUMMARIES:
        assert client.get(f"/monthly-summary/{month['slug']}").status_code == 200, month['slug']


def test_browse_api_filters(client):
    _login(client)
    may = client.get('/api/browse?month=may').get_json()
    assert may['count'] >= 4
    assert all(c['month_slug'] == 'may' for c in may['campaigns'])

    sw1 = client.get('/api/browse?store=SW1').get_json()
    assert sw1['count'] >= 3
    assert all('SW1' in c['stores'] for c in sw1['campaigns'])

    family = client.get('/api/browse?family=sandwich-deal').get_json()
    assert family['count'] == 3


def test_chat_month_and_family(client):
    _login(client)
    may = client.post('/api/chat', json={'query': 'Summarize May like the August story'}).get_json()
    assert 'May' in may['answer']
    assert may['campaigns']
    assert may['formatted']['headline']
    assert isinstance(may['formatted']['bullets'], list)
    assert any('May' in b for b in may['formatted']['bullets'])
    assert may['metrics']
    assert all(m.get('month') for m in may['metrics'])

    coffee = client.post('/api/chat', json={'query': 'Show the free coffee family across months'}).get_json()
    assert 'Coffee' in coffee['answer'] or 'coffee' in coffee['answer'].lower()
    assert coffee['campaigns']
    assert coffee['formatted']['headline']
    joined = ' '.join(coffee['formatted']['bullets'])
    assert 'May' in joined and ('June' in joined or 'July' in joined)

    fw = generate_chat_answer('Fireworks story May–August')
    assert 'June' in fw or 'summer' in fw.lower() or 'Fireworks' in fw
    assert 'HEADLINE:' in fw or 'June' in fw


def test_knowledge_helpers():
    assert len(MONTHLY_STORIES) == 4
    assert len(CAMPAIGN_FAMILIES) == 3
    assert len(ALL_CAMPAIGN_CARDS) >= 18
    ans, camps, _ = answer_from_knowledge('What happened at TGC?')
    assert 'TGC' in ans
    assert camps


def test_chat_guardrail_and_audit_log(client):
    _login(client)
    refused = client.post('/api/chat', json={'query': 'Tell me a joke about crypto'}).get_json()
    assert refused['on_topic'] is False
    assert 'campaign' in refused['formatted']['headline'].lower() or 'CAA' in refused['formatted']['headline']
    assert refused['disclaimer']

    ok = client.post('/api/chat', json={'query': 'Summarize August results with metrics'}).get_json()
    assert ok['on_topic'] is True
    assert ok['disclaimer']
    assert ok['metrics']

    log = client.get('/api/chat-log?limit=20').get_json()
    assert log['count'] >= 2
    queries = [t['query'] for t in log['turns']]
    assert 'Tell me a joke about crypto' in queries
    assert 'Summarize August results with metrics' in queries

    page = client.get('/chat-log')
    assert page.status_code == 200
    assert b'Chat audit log' in page.data or b'Campaign chat log' in page.data


def test_healthcheck_reports_archive(client):
    response = client.get('/api/healthcheck')
    assert response.status_code == 200
    payload = response.get_json()
    assert payload['status'] == 'ok'
    assert payload['archive_html_files'] >= 20
