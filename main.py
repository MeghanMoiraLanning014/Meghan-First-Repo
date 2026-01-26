# main.py
from note_service import add_note, list_notes, search_notes

def main():
    while True:
        print("\nNotes App")
        print("1. Add Note")
        print("2. List Notes")
        print("3. Search Notes")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            text = input("Enter note: ")
            add_note(text)
            print("Note added!")
        elif choice == "2":
            notes = list_notes()
            if notes:
                print("\nYour Notes:")
                for i, note in enumerate(notes, 1):
                    print(f"{i}. {note}")
            else:
                print("No notes yet.")
        elif choice == "3":
            keyword = input("Enter keyword to search: ")
            results = search_notes(keyword)
            if results:
                print("\nSearch Results:")
                for i, note in enumerate(results, 1):
                    print(f"{i}. {note}")
            else:
                print("No matching notes.")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
