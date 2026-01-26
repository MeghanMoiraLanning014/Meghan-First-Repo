# file_store.py

NOTES_FILE = "notes.txt"

def read_notes():
    """Return a list of notes"""
    try:
        with open(NOTES_FILE, "r") as f:
            notes = f.read().splitlines()
    except FileNotFoundError:
        notes = []
    return notes

def write_notes(notes):
    """Write a list of notes to the file"""
    with open(NOTES_FILE, "w") as f:
        f.write("\n".join(notes))
