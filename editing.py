# Lets the user add, delete, update, or view words in a unit.
# Everything related to editing the vocab.

from input_validation import confirm_del_action
from file_ops import load_vocab, save_vocab, save_vocab_file


#function that adds a word to the dictionary
def add_word() -> None:
    vocab = load_vocab()

    while True:
        # Show available units
        if vocab:
            print(f"\nAvailable units: {', '.join(vocab.keys())}")
        else:
            print("\nNo units yet in the vocabulary.")

        choice = input("Do you want to add a new sword to an existing unit or create a new one? (type 'existing' or 'new', or 'exit' to return): ").strip().lower()

        if choice == "exit":
            print("Returning to main menu.")
            return

        if choice == "existing":
            unit = input("Enter the name of the existing unit: ").strip().lower()
            if unit not in vocab:
                print(f"Unit '{unit}' does not exist. Please try again.")
                continue

        elif choice == "new":
            while True:
                unit = input("Enter a name for the new unit: ").strip().lower()
                if unit in vocab:
                    print("This unit already exists. Please choose a different name.")
                else:
                    vocab[unit] = []
                    print(f"Created new unit '{unit}'.")
                    break
        else:
            print("Invalid choice. Please type 'existing', 'new', or 'exit'.")
            continue

        # Add word to the chosen unit
        word = input("Enter the word to add: ").strip().lower()
        meaning = input(f"What is the meaning of '{word}': ").strip()

        # Check for duplicates
        if any(entry["word"].lower() == word for entry in vocab[unit]):
            print(f"The word '{word}' already exists in unit '{unit}'.")
        else:
            vocab[unit].append({"word": word, "meaning": meaning})
            save_vocab_file(vocab)
            print(f"The word '{word}' was added to unit '{unit}'.")

        # Ask if the user wants to add another word
        again = input("Do you want to add another word? (yes/no): ").strip().lower()
        if again != "yes":
            print("Returning to main menu.")
            return



#function that delets a word in the dictionary
def delete_word() -> None:
    vocab = load_vocab()
    while True:
        word_to_delete = input("Which word do you want to delete? (type 'exit' to return to main menu): ").strip().lower()
        if word_to_delete == "exit":
            print("Returning to main menu.")
            return
        # checking in which units the word exists
        units_with_word = []
        for unit_name in vocab:
            for entry in vocab[unit_name]:
                if entry["word"].strip().lower() == word_to_delete:
                    units_with_word.append(unit_name)
                    break  
        if not units_with_word:
            print(f"The word '{word_to_delete}' was not found in any unit.")
            continue
        else:
            # in case the word was found in unit/s
            print(f"The word '{word_to_delete}' appears in the following unit(s): {', '.join(units_with_word)}")

            if confirm_del_action(f"Do you want to delete the word '{word_to_delete}' from these unit(s)?"):
                for unit_name in units_with_word:
                    vocab[unit_name] = [entry for entry in vocab[unit_name] if entry["word"].lower() != word_to_delete]
                save_vocab(vocab)
                print(f"The word '{word_to_delete}' was deleted from: {', '.join(units_with_word)}")
                return
            else:
                return


#function that delets a whole unit
def delete_unit() -> None:
    vocab = load_vocab()
    while True:
        unit_to_delete = input("Which unit do you want to delete? (type 'exit' to return to main menu): ").strip().lower()
        if unit_to_delete == "exit":
            print("Returning to main menu.")
            return
        if unit_to_delete not in vocab:
            print(f"'{unit_to_delete}' was not found in the dictionary.")
            continue
        else:
            # in case the unit was found in dictionary
            print(f"'{unit_to_delete}' exists in the dictionary")
        if confirm_del_action(f"Do you want to delete '{unit_to_delete}' from the dictionary?"):
            del vocab[unit_to_delete]
            save_vocab_file(vocab)
            print(f"'{unit_to_delete}' was deleted from the dictionary.")
            return
        else:
            return



#finction that shows the words and their translation from a unit
def list_words() -> None:
    vocab = load_vocab()
    
    while True:
        words_to_display = input("Would you like to list words from all units or specific units? (type 'all' or 'choose'): ").strip().lower()
        if words_to_display == "all":
            print("\nHere are all the words from all the units in the vocabulary:\n")
            for unit, word_list in vocab.items():
                print(f"{unit}")
                for entry in word_list:
                    print(f"  - {entry['word']}: {entry['meaning']}")
            return
        elif words_to_display == "choose":
            available_units = list(vocab.keys())
            print(f"\nAvailable units: {', '.join(available_units)}")
            chosen_units = input("Enter unit names separated by commas (e.g., unit_1, unit_3): ").strip().lower().split(",")
            for unit in chosen_units:
                unit = unit.strip()
                if unit in vocab:
                    print(f"\n{unit}")
                    for entry in vocab[unit]:
                        print(f"  - {entry['word']}: {entry['meaning']}")
                else:
                    print(f"\nUnit '{unit}' does not exist in the vocabulary.")
            return

        else:
            print("Invalid choice. Please type 'all' or 'choose'.")

