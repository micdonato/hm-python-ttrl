# tests/test_console.py
# from unittest.mock import Mock

import click.testing
import pytest
import requests

# idiota ricordati che hai cambiato nome al pacchetto
from hm_python_ttrl import console


@pytest.fixture
def mock_requests_get(mocker):
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Lorem Ipsum",
        "extract": "Lorem ipsum dolor sit amet",
    }
    # DO NOT FUCKING FORGET TO RETURN MOCK
    return mock


@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_main_succeeds(runner, mock_requests_get):
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_prints_title(runner, mock_requests_get):
    result = runner.invoke(console.main)
    print(result.output)
    assert "Lorem Ipsum" in result.output


# check what were the parameters passed to the request
def test_main_uses_en_wikipedia_org(runner, mock_requests_get):
    runner.invoke(console.main)
    args, _ = mock_requests_get.call_args
    assert "en.wikipedia.org" in args[0]


# Simulate an error on the request
def test_main_fails_on_request_error(runner, mock_requests_get):
    mock_requests_get.side_effect = Exception("Boom")
    result = runner.invoke(console.main)
    assert result.exit_code == 1


# without modifying the wikipedia.py as well this won't work
# because click does not deal with it (doesn't raise it?)
# so the guy uses a try catch block, catches request (launched by the mock)
# and raises clickexception, which prints "error" somewhere in the output
def test_main_prints_message_on_request_error(runner, mock_requests_get):
    mock_requests_get.side_effect = requests.RequestException
    result = runner.invoke(console.main)
    assert "Error" in result.output
