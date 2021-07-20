# tests/test_console.py
import click.testing
import pytest

#idiota ricordati che hai cambiato nome al pacchetto
from hm_python_ttrl import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_main_succeeds(runner):
    result = runner.invoke(console.main)
    assert result.exit_code == 0