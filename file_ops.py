# Handles loading and saving data from JSON files - vocabulary and settings
# Used for both the vocabulary and the settings.

import json
import os
from S3utils import download_file_from_s3, upload_file_to_s3

VOCAB_FILE = "vocab.json"
SETTINGS_FILE = "settings.json"

# Load settings from S3

def load_settings():
    download_file_from_s3(SETTINGS_FILE, SETTINGS_FILE)
    if not os.path.exists(SETTINGS_FILE):
        print("No settings file found. Creating a new settings file")
        return {
            "global": {
                "delay_seconds": 3,
                "repeat_count": 7
            },
            "unit_overrides": {}
        }

    with open(SETTINGS_FILE, "r", encoding="utf-8") as settings_file:
        return json.load(settings_file)

# Save settings to S3
def save_settings(settings_data):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as sett_file:
        json.dump(settings_data, sett_file, indent=4, ensure_ascii=False)
    upload_file_to_s3(SETTINGS_FILE, SETTINGS_FILE)


# Load vocabulary from S3
def load_vocab():
    download_file_from_s3(VOCAB_FILE, VOCAB_FILE)
    if not os.path.exists(VOCAB_FILE):
        print("No vocabulary file found. Starting with empty vocabulary.")
        return {}

    with open(VOCAB_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

# Save a new word to the vocabulary and upload to S3
def save_vocab(unit: str, word: str, meaning: str) -> None:
    vocab = load_vocab()
    if unit not in vocab:
        vocab[unit] = []

    for entry in vocab[unit]:
        if entry["word"] == word:
            entry["meaning"] = meaning
            break
    else:
        vocab[unit].append({"word": word, "meaning": meaning})

    with open(VOCAB_FILE, "w", encoding="utf-8") as file:
        json.dump(vocab, file, indent=2, ensure_ascii=False)
    upload_file_to_s3(VOCAB_FILE, VOCAB_FILE)

# Save entire vocabulary file and upload to S3
def save_vocab_file(data: dict) -> None:
    with open(VOCAB_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    upload_file_to_s3(VOCAB_FILE, VOCAB_FILE)
