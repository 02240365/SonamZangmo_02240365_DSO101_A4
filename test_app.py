import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Basic math test (as shown in assignment)
def test_basic_math():
    assert 1 + 1 == 2

# Test home route
def test_home(client):
    res = client.get('/')
    assert res.status_code == 200
    data = res.get_json()
    assert data['message'] == 'TaskFlow API is running'
    assert data['student_id'] == '02240365'

# Test health check
def test_health(client):
    res = client.get('/health')
    assert res.status_code == 200
    assert res.get_json()['status'] == 'OK'

# Test get tasks returns list
def test_get_tasks(client):
    res = client.get('/tasks')
    assert res.status_code == 200
    assert isinstance(res.get_json(), list)

# Test add task
def test_add_task(client):
    res = client.post('/tasks',
        json={'title': 'Buy groceries'},
        content_type='application/json'
    )
    assert res.status_code == 201
    data = res.get_json()
    assert data['title'] == 'Buy groceries'
    assert data['completed'] == False

# Test add task without title returns 400
def test_add_task_no_title(client):
    res = client.post('/tasks',
        json={},
        content_type='application/json'
    )
    assert res.status_code == 400
    assert res.get_json()['error'] == 'Title is required'
