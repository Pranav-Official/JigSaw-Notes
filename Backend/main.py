import flask
from flask import request, jsonify, Flask
import json
import pymongo

import NoteBooks
import QuickNotes

from pymongo import MongoClient

client = MongoClient()
db = client["Notes"]
QuickNotesCollection = db["QuickNotes"]
NoteBooksCollection = db["Notebooks"]


app = Flask(__name__)

@app.route('/data', methods=['GET', 'POST'])
def send_data():
    if request.method == 'GET':
        # Generate sample data
        data = NoteBooks.GetNoteBooks(NoteBooksCollection)
        
        # Return data as JSON response
        return data
    
    elif request.method == 'POST':
        # Get data from request body
        data = request.get_json()
        
        # Return received data as JSON response
        return jsonify(data)