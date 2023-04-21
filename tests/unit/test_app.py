import os

import pytest

from src.app import one_and_one
from src.print import print_something
from src.write_file import write_text_to_file_path


@pytest.mark.math
def test_one_and_one():
    result = one_and_one()
    expected_result = 2
    assert result == expected_result


@pytest.mark.notmath
def test_capture():
    print_something()


def test_capture_with_fixture(capsys):
    print_something()
    captured = capsys.readouterr()
    assert captured.out == "This is a test.\n"


def test_project_id(project_id):
    project_id = os.environ["PROJECT_ID"]
    print(f"project_id is {project_id}.")


#  tmp_path
def test_tmp_path(tmp_path):
    path_location = str(tmp_path)
    print(path_location)


def test_file_content(tmp_path):
    text = "text"
    file_path = tmp_path / "text.txt"
    write_text_to_file_path(text, file_path)

    # assert file exists
    assert file_path.exists()

    with open(str(file_path), "r") as file:
        result = file.read()

    # assert file content
    assert result == text
