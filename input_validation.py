# Checks and cleans the user's input.
# Makes sure there are no empty words, duplicates, etc.


#confirmation of action - before deleting something - calidate confirmation
def confirm_del_action(message: str) -> bool:
    confirm = input(f"{message} (yes/no): ")
    if confirm.strip().lower() == "yes":
        return True 
    else:
        print("Deletion canceled.")
        return False
        
    