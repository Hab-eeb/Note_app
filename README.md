# Flask Note-Taking Application

This is a robust note-taking application built with Flask, featuring a RESTful API backend. The project is continuously evolving, with plans for a full-fledged frontend in the future.

## Current Features

- RESTful API for note management
- Create, read, update, and delete notes
- User authentication
- Search notes by title

## Roadmap

- Frontend development
- Enhanced user features
- Mobile responsiveness

## Setup

1. Clone the repository
2. Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate # On MAC use 
venv\Scripts\activate # On Windows use

3. Install dependencies: `pip install -r requirements.txt`
4. Run the application: `flask run`

## API Endpoints

- POST /notes: Create a new note
- GET /notes/<id>: Retrieve a note by ID
- PUT /notes/<id>: Update a note
- DELETE /notes/<id>: Delete a note
- GET /notes: List all notes
- GET /notes/search?q=<query>: Search notes by title

## Testing

Run tests using pytest: `pytest test_app.py`

## Contributing

This is a personal project aimed at improving Python and Flask skills. While it's not open for contributions at this time, feel free to fork the repository and adapt it for your own learning purposes.
