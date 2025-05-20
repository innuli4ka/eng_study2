# Shows English words and waits before showing the meaning.
# Uses settings for delay and repeat count.
# User can choose which unit or which words to train.


from file_ops import load_vocab, load_settings
import time

# this function runs the training mode
# user chooses a unit, optionally a word range
# for each word: shows it, waits, then shows the meaning, multiple times

def training_mode():
    vocab = load_vocab()
    settings = load_settings()

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
            unit_choice = int(input("\nEnter the number of the unit you want to train on (e.g. 1 or 2 or 3.....): ").strip())
            unit = unit_list[unit_choice - 1]
            break
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number from the list.")

    words = vocab[unit]
    if not words:
        print(f"Unit '{unit}' has no words to train on.")
        return

    print(f"There are {len(words)} words in '{unit}'.")

    # Show list of words with their indexes
    print("\nWords in this unit:")
    for idx, entry in enumerate(words, 1):
        print(f"  {idx}. {entry['word']} — {entry['meaning']}")

    use_range = input("\nWould you like to train on a specific word range? (yes/no): ").strip().lower()

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

    # get settings for this unit or fallback to global
    unit_settings = settings.get("unit_overrides", {}).get(unit, {})
    delay = unit_settings.get("delay_seconds", settings["global"].get("delay_seconds", 3))
    repeat = unit_settings.get("repeat_count", settings["global"].get("repeat_count", 7))

    print(f"\nStarting training for unit '{unit}' with delay {delay}s and {repeat} repetitions per word.\n")

    for _ in range(repeat):
        for entry in words:
            print(f"Word: {entry['word']}")
            for i in range(delay, 0, -1):
                print(f"Translation in: {i} seconds...", end="\r")
                time.sleep(1)
            print(f"Meaning: {entry['meaning']}\n")

    print("Training complete.")
