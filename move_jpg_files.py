"""
Task 3 - Move all .jpg files from one folder to a new folder.
Uses: os, shutil (file handling)
"""

import os
import shutil

SOURCE_FOLDER = "source_folder"
DEST_FOLDER = "jpg_images"

SAMPLE_JPEG = (
    b"\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00"
    b"\xff\xdb\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t\x08\n\x0c"
    b"\x14\r\x0c\x0b\x0b\x0c\x19\x12\x13\x0f\x14\x1d\x1a\x1f\x1e\x1d\x1a\x1c"
    b"\x1c $.\' \",#\x1c\x1c(7),01444\x1f'9=82<.342\xff\xc0\x00\x0b\x08\x00"
    b"\x01\x00\x01\x01\x01\x11\x00\xff\xc4\x00\x14\x00\x01\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\xff\xc4\x00\x14\x10\x01\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xda\x00\x08\x01\x01\x00\x00?\x00"
    b"\x7f\xff\xd9"
)


def get_jpg_files(folder):
    if not os.path.exists(folder):
        return []
    return [
        f for f in os.listdir(folder)
        if f.lower().endswith((".jpg", ".jpeg"))
        and os.path.isfile(os.path.join(folder, f))
    ]


def create_sample_images(source):
    print(f"Creating sample images in '{source}'...\n")
    for name in ("photo1.jpg", "photo2.jpg"):
        with open(os.path.join(source, name), "wb") as f:
            f.write(SAMPLE_JPEG)


def move_jpg_files(source, destination):
    """Move all .jpg and .jpeg files from source to destination."""
    os.makedirs(source, exist_ok=True)
    os.makedirs(destination, exist_ok=True)

    source_files = get_jpg_files(source)
    dest_files = get_jpg_files(destination)

    # First run: no files anywhere -> create samples then move
    if not source_files and not dest_files:
        create_sample_images(source)
        source_files = get_jpg_files(source)

    # Already done from a previous run
    if not source_files and dest_files:
        print(f"All images are already in '{destination}':")
        for name in dest_files:
            print(f"  - {name}")
        print("\nTo move more, add new .jpg files to 'source_folder' and run again.")
        return

    moved_count = 0
    for filename in source_files:
        source_path = os.path.join(source, filename)
        dest_path = os.path.join(destination, filename)

        shutil.move(source_path, dest_path)
        print(f"Moved: {filename}")
        moved_count += 1

    print(f"\nDone! Moved {moved_count} image(s) to '{destination}'.")


if __name__ == "__main__":
    move_jpg_files(SOURCE_FOLDER, DEST_FOLDER)
