# clean_data.py

import os
import hashlib
import shutil

# --- Configuration ---
DATA_DIR = 'data'
TRAINING_DIR = os.path.join(DATA_DIR, 'training')
VALIDATION_DIR = os.path.join(DATA_DIR, 'validation')

def get_file_hash(filepath):
    """Calculates the SHA256 hash of a file for unique identification."""
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()

def get_all_training_hashes():
    """Generates a set of hashes for all images in the training folder."""
    training_hashes = set()
    print("Indexing training files...")
    for monument_class in os.listdir(TRAINING_DIR):
        class_path = os.path.join(TRAINING_DIR, monument_class)
        if os.path.isdir(class_path):
            for filename in os.listdir(class_path):
                filepath = os.path.join(class_path, filename)
                if os.path.isfile(filepath):
                    try:
                        training_hashes.add(get_file_hash(filepath))
                    except Exception as e:
                        print(f"Skipping file {filepath}: {e}")
    print(f"Found {len(training_hashes)} unique training images.")
    return training_hashes

def remove_duplicate_validation_files(training_hashes):
    """Checks validation files against training hashes and removes duplicates."""
    duplicates_found = 0
    print("\nChecking validation files for duplicates...")
    for monument_class in os.listdir(VALIDATION_DIR):
        class_path = os.path.join(VALIDATION_DIR, monument_class)
        if os.path.isdir(class_path):
            files_to_check = list(os.listdir(class_path))
            for filename in files_to_check:
                filepath = os.path.join(class_path, filename)
                if os.path.isfile(filepath):
                    file_hash = get_file_hash(filepath)
                    if file_hash in training_hashes:
                        print(f"DUPLICATE FOUND: Deleting {filepath}")
                        os.remove(filepath)
                        duplicates_found += 1
    
    print(f"\nCompleted cleanup. Total duplicates removed from validation set: {duplicates_found}")
    if duplicates_found > 0:
        print("NOTE: You will need to manually replace the deleted validation images with NEW, unique photos.")
    return duplicates_found

if __name__ == '__main__':
    # 1. Check if directories exist
    if not os.path.isdir(TRAINING_DIR) or not os.path.isdir(VALIDATION_DIR):
        print("ERROR: Training or Validation directories not found in the 'data/' folder. Please check your path.")
    else:
        # 2. Get hashes of all training files
        hashes = get_all_training_hashes()
        
        # 3. Remove validation files matching those hashes
        duplicates = remove_duplicate_validation_files(hashes)

        if duplicates > 0:
            print("\n🚨 CRITICAL: Duplicates removed. You MUST add new, unique images to the validation folders before training.")
        else:
            print("\n✅ SUCCESS: No duplicates found! Your data is ready for final training.")
