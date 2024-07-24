from flask import Blueprint, request, jsonify
from app import db
from app.models import Note

# Create a Flask blueprint
app = Blueprint('app', __name__)

# Define routes within the blueprint
@app.route('/hello')
def hello():
    return 'Hello, Flask!'

#Create a new note
@app.route('/notes', methods=['POST'])
def create_note():
    data = request.get_json()
    new_note = Note(
        title = data['title'],
        content = data['content']
    )
    db.session.add(new_note)
    db.session.commit()
    return jsonify({'message':'Note created!'}),201

#Retrieve a note by ID
@app.route('/notes/<int:id>', methods=['GET'])
def get_note(id):
    note = Note.query.get(id)
    if not note:
        return jsonify({'message':'Note not found!'}), 404
    return jsonify({
        'id': note.id,
        'title': note.title,
        'content': note.content
    }), 200

#Update a note by ID 
@app.route('/notes/<int:id>',methods = ['PUT'])
def update_note(id):
    data = request.get_json()
    note = Note.query.get(id)
    if not note:
        return jsonify({'message':'Note not found!'}), 404
    note.title = data['title']
    note.content = data['content']
    db.session.commit()
    return jsonify({'message': 'Note updated'}), 200

#Delete a note by ID 
@app.route('/notes/<int:id>', methods=['DELETE'])
def delete_note(id):
    note = Note.query.get(id)
    if not note:
        return jsonify({'message':'Note not found!'}), 404
    db.session.delete(note)
    db.session.commit()
    return jsonify({'message': 'Note deleted!'}), 200

#List all notes 
@app.route('/notes', methods =['GET'] )
def get_all_notes():
    notes = Note.query.all()
    notes_list = [{'id':note.id, 'title':note.title, 'content':note.content} for note in notes]
    return jsonify(notes_list), 200

#Search notes by title
@app.route('/notes/search', methods = ['GET'])
def search_notes():
    query = request.args.get('q')
    notes = Note.query.filter(Note.title.contains(query)).all()
    notes_list = [{'id':note.id, 'title':note.title, 'content':note.content} for note in notes]
    return jsonify(notes_list), 200

