import pytest
from app import create_app, db
from app.models import Note
import json

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'


    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

    
    with app.app_context():
        db.drop_all()

def test_create_note(client):
    response = client.post('/notes', 
                           data = json.dumps({'title':'Test Note',
                        'content':'This is a test' }),
                        content_type ='application/json'
                           )
    assert response.status_code == 201
    assert b'Note created!' in response.data

def test_get_note(client):
    #first, create a note
    client.post('/notes',
                data = json.dumps({
                    'title':"Test Note",
                    'content':"This is a test"
                }),
                content_type ='application/json'
                )
    #Now try to get the note
    response = client.get('/notes/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['title'] == 'Test Note'
    assert data['content'] == 'This is a test'

def test_update_note(client):
    #First , create a note
    client.post('/notes',
                data = json.dumps({'title':'Test Note',
                                   'content':'This is a test'}),
                                   content_type = 'application/json'
                )
    # Now update the note 
    response = client.put('/notes/1',
                          data = json.dumps({
                              'title':'Updated Note',
                              'content':'This is updated'
                          }),
                          content_type = 'application/json'
                          )
    
    assert response.status_code == 200
    assert b'Note updated' in response.data
    
    #Check if the note was actually updated
    response = client.get('/notes/1')
    data = json.loads(response.data)
    assert data['title'] == 'Updated Note'
    assert data['content'] == 'This is updated'


def test_delete_note(client):
    #First, create a note 
    client.post('/notes',
                data = json.dumps({'title':'Test Note',
                                   'content':'This is a test'}),
                    content_type = 'application/json'
                )
    #Now delete the note
    response = client.delete('/notes/1')
    assert response.status_code == 200
    assert b'Note deleted!' in response.data 

    #Try to get the deleted note
    response = client.get('/notes/1')
    assert response.status_code == 404

def test_get_all_notes(client):
    #Create multiple notes 
    client.post('/notes', 
              data=json.dumps({'title': 'Note 1', 'content': 'Content 1'}),
              content_type='application/json')
    client.post('/notes', 
              data=json.dumps({'title': 'Note 2', 'content': 'Content 2'}),
              content_type='application/json')
    
    #Get all notes 
    response = client.get('/notes')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 2
    assert data[0]['title'] == 'Note 1'
    assert data[1]['title'] == 'Note 2'

def test_search_notes(client):
    #Create multiple notes 
    client.post('/notes', 
              data=json.dumps({'title': 'Apple', 'content': 'Red fruit'}),
              content_type='application/json')
    client.post('/notes', 
              data=json.dumps({'title': 'Banana', 'content': 'Yellow fruit'}),
              content_type='application/json')
    
    #Search for notes 
    response = client.get('/notes/search?q=Apple')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1
    assert data[0]['title'] == 'Apple'

