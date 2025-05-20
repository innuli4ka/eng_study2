# This is the main UI for the vocabulary app.
# The user chooses what mode they want to run.

from editing import add_word, delete_word, delete_unit, list_words
from training import training_mode
from testing import testing_mode
from settings import show_settings, update_setting
from S3utils import download_file_from_s3, upload_file_to_s3

def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Add a word")
        print("2. Delete a word")
        print("3. Delete a unit")
        print("4. List words")
        print("5. Training mode")
        print("6. Testing mode")
        print("7. Show settings")
        print("8. Update settings")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            add_word()
        elif choice == "2":
            unit = input("Enter the unit name: ").strip().lower()
            word = input("Enter the word to delete: ").strip().lower()
            delete_word(unit, word)
        elif choice == "3":
            delete_unit()
        elif choice == "4":
            list_words()
        elif choice == "5":
            training_mode()
        elif choice == "6":
            testing_mode()
        elif choice == "7":
            show_settings()
        elif choice == "8":
            update_setting()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()

