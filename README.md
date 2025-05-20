Vocabulary Trainer – README

This is a CLI-based tool to help you manage and train your vocabulary efficiently.

What it does

Lets you add and manage vocabulary words by units

Supports training mode with timed word display

Supports testing mode to check your knowledge

Settings are flexible per unit or globally (delay & repetitions)

Data is saved to and loaded from S3

How to use

1. Start the app:

python main.py

2. Menu options:

1. Add a word
2. Delete a word
3. Delete a unit
4. List words
5. Training mode
6. Testing mode
7. Show settings
8. Update settings
9. Exit

Settings

Settings can be updated globally or per unit:

Delay (in seconds) between word and translation

Number of repetitions per word during training

Stored in settings.json (fetched and uploaded via S3 automatically).

File storage via S3
