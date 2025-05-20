# this function runs the testing mode
# user chooses a unit and optionally a word range
# for each word: show the word and ask user for the translation
# compare the answer and track how many were correct

from file_ops import load_vocab

def testing_mode():
    vocab = load_vocab()

    if not vocab:
        print("There are no units available.")
        return

    # display numbered list of units
    unit_list = list(vocab.keys())
    print("\nAvailable units:")
    for idx, unit in enumerate(unit_list, 1):
        print(f"  {idx}. {unit}")

    while True:
        try:
            unit_choice = int(input("\nEnter the number of the unit you want to test (e.g. 1 or 2 or 3...): ").strip())
            unit = unit_list[unit_choice - 1]
            break
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number from the list.")

    words = vocab[unit]
    if not words:
        print(f"Unit '{unit}' has no words to test.")
        return

    print(f"There are {len(words)} words in '{unit}'.")

    # Show list of words with their indexes
    print("\nWords in this unit:")
    for idx, entry in enumerate(words, 1):
        print(f"  {idx}. {entry['word']} — {entry['meaning']}")

    use_range = input("\nWould you like to test on a specific word range? (yes/no): ").strip().lower()

    if use_range == "yes":
        try:
            word_input = input("Enter start and end words (in English or translated), separated by comma: ").strip().split(",")
            if len(word_input) != 2:
                print("Please provide exactly two words separated by a comma.")
                return
            start_word, end_word = word_input[0].strip(), word_input[1].strip()

            start_index = next(i for i, entry in enumerate(words) if entry['word'] == start_word or entry['meaning'] == start_word)
            end_index = next(i for i, entry in enumerate(words) if entry['word'] == end_word or entry['meaning'] == end_word) + 1

            words = words[start_index:end_index]
        except (StopIteration, ValueError):
            print("Invalid range. Make sure the words exist in the list.")
            return

    print(f"\nStarting test for unit '{unit}'. Type your answer and press Enter.\n")
    correct = 0
    total = len(words)
    incorrect_answers = []

    for entry in words:
        user_answer = input(f"What is the translation of '{entry['word']}'? ").strip()
        if user_answer == entry['meaning']:
            print("Correct!\n")
            correct += 1
        else:
            print(f"Incorrect. The correct answer is: {entry['meaning']}\n")
            incorrect_answers.append((entry['word'], entry['meaning']))

    score_percent = (correct / total) * 100

    print(f"Test complete. You got {correct} out of {total} correct.")
    print(f"Score: {score_percent:.0f}%")

    if score_percent >= 85:
        print("Excellent! Great job remembering your vocabulary.")
    elif score_percent >= 60:
        print("Good work! A bit more practice and you'll master it.")
    elif score_percent >= 30:
        print("Keep going! You're getting there, but review needed.")
    else:
        print("Needs improvement. Study the words again and try once more.")

    if incorrect_answers:
        print("\nWords to review:")
        for word, correct_meaning in incorrect_answers:
            print(f"  - {word}: {correct_meaning}")
            

