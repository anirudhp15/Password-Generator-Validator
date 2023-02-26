from project import ask_to_continue, generate_pass, validate_pass, score_pass
import pytest
from unittest.mock import Mock, patch


def main():
    test_ask_to_continue()
    test_generate_pass()
    test_validate_pass()
    test_score_pass()


def test_ask_to_continue() -> None:
    with patch('builtins.input', new=Mock(return_value='yes')):
        assert ask_to_continue() == True
    with patch('builtins.input', new=Mock(return_value='no')):
        assert ask_to_continue() == False
    with patch('builtins.input', new=Mock(return_value='nope')):
        assert ask_to_continue() == None


def test_generate_pass() -> None:
    with patch('builtins.input', new=Mock(return_value='complicated')):
        assert generate_pass() == None


def test_validate_pass():
    with patch('builtins.input', new=Mock(return_value='Password15$')):
        assert validate_pass() == None


def test_score_pass():
    assert score_pass("Password15$") == (10, 'None!')


if __name__ == "__main__":
    main()