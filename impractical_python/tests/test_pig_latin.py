from pig_latin.pigLatin import *
import pytest
import mock

input_output_data = [
    ("hello world", "\nellohay orldway\n"),
    ("HElLo woRLD", "\nellohay orldway\n"),
    ("Art is fun", "\nartway isway unfay\n"),
    ("Orange you glad", "\norangeway ouyay ladgay\n")
]


@pytest.mark.parametrize("sentence, expected", input_output_data)
def test_pigify(sentence, expected):
    assert pigify(sentence) == expected