# Lets the user show, update, save the settings
# Everything related to actions in settings
from file_ops import save_settings, load_settings, load_vocab

#this function shows the global or per unit settings
def show_settings() -> None:
    settings = load_settings()

    print("\n Global Settings:")
    print(f"  Delay between word and translation: {settings['global']['delay_seconds']} seconds")
    print(f"  Number of repetitions per word: {settings['global']['repeat_count']} times")

    unit_overrides = settings.get("unit_overrides", {})
    if unit_overrides:
        print("\n Unit-specific overrides:")
        for unit, overrides in unit_overrides.items():
            delay = overrides.get("delay_seconds", "(default)")
            repeat = overrides.get("repeat_count", "(default)")
            print(f"  {unit} → Delay: {delay}, Repetitions: {repeat}")
    else:
        print("\nNo unit-specific overrides found.")
        




def update_setting():
    # Load current settings from the settings.json file
    settings = load_settings()

    # Ask the user if they want to update global settings or unit-specific settings
    choice = input("Would you like to update settings for all units or for a specific unit? (type 'global' or 'unit'): ").strip().lower()

    if choice == "global":
        # User chose to update global settings
        print("\nWhat would you like to update?")
        print("1. Delay between word and translation")
        print("2. Number of repetitions per word")
        setting_choice = input("Enter 1 or 2: ").strip()

        if setting_choice == "1":
            # Update global delay
            try:
                new_value = int(input("Enter new delay time in seconds (e.g., 3): ").strip())
                settings["global"]["delay_seconds"] = new_value
                print(f"Updated global delay to {new_value} seconds.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif setting_choice == "2":
            # Update global repeat count
            try:
                new_value = int(input("Enter new number of repetitions (e.g., 7): ").strip())
                settings["global"]["repeat_count"] = new_value
                print(f"Updated global repetitions to {new_value}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("Invalid choice. Please select 1 or 2.")

        # Save the updated global settings
        save_settings(settings)

    elif choice == "unit":
        # User chose to update settings for a specific unit
        vocab = load_vocab()
        available_units = list(vocab.keys())

        if not available_units:
            print("No units available in the vocabulary.")
            return

        # Show list of existing units
        print("\nAvailable units:")
        for unit in available_units:
            print(f"  - {unit}")

        # Ask the user which unit to update
        unit_name = input("\nEnter the name of the unit you want to update: ").strip().lower()

        if unit_name not in available_units:
            print(f"Unit '{unit_name}' does not exist.")
            return

        print("\nWhat would you like to update?")
        print("1. Delay between word and translation")
        print("2. Number of repetitions per word")
        setting_choice = input("Enter 1 or 2: ").strip()

        # Ensure the unit has a place in the overrides section
        if unit_name not in settings["unit_overrides"]:
            settings["unit_overrides"][unit_name] = {}

        if setting_choice == "1":
            # Update unit-specific delay
            try:
                new_value = int(input("Enter new delay time in seconds (e.g., 3): ").strip())
                settings["unit_overrides"][unit_name]["delay_seconds"] = new_value
                print(f"Updated delay for '{unit_name}' to {new_value} seconds.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif setting_choice == "2":
            # Update unit-specific repeat count
            try:
                new_value = int(input("Enter new number of repetitions (e.g., 7): ").strip())
                settings["unit_overrides"][unit_name]["repeat_count"] = new_value
                print(f"Updated repetitions for '{unit_name}' to {new_value}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("Invalid choice. Please select 1 or 2.")

        # Save the updated unit-specific settings
        save_settings(settings)

    else:
        print("Invalid choice. Please type 'global' or 'unit'.")
        
