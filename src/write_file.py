from pathlib import Path


def write_text_to_file_path(text: str, file_path: Path):
    with open(file_path, "w") as file:
        file.write(text)
