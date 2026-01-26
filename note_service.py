# note_service.py
from file_store import read_notes, write_notes

def add_note(text):
    notes = read_notes()
    notes.append(text)
    write_notes(notes)

def list_notes():
    return read_notes()

def search_notes(keyword):
    notes = read_notes()
    return [note for note in notes if keyword.lower() in note.lower()]
