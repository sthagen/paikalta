import pathlib

import paikalta.cli as cli
from paikalta import FAIL, SUCC

FIXTURES_UPSTREAM = pathlib.Path('test', 'fixtures', 'upstream')
VALID_NAME = FIXTURES_UPSTREAM / 'valid' / 'oasis_csaf_tc-csaf_2_0-2021-5-1-11.json'
INVALID_NAME = FIXTURES_UPSTREAM / 'invalid' / 'OASIS_CSAF_TC-CSAF_2.0-2021-5-1-01.json'


def test_parser():
    assert cli.parser()


def test_app_valid():
    assert cli.app([str(VALID_NAME)]) == 0


def test_app_invalid():
    assert cli.app([str(INVALID_NAME)]) == 1


def test_app_valid_echo(capsys):
    assert cli.app([str(VALID_NAME), '-p']) == 0
    out, err = capsys.readouterr()
    assert str(VALID_NAME.name) in out
    assert not err


def test_app_invalid_echo(capsys):
    assert cli.app([str(INVALID_NAME), '-p']) == 1
    out, err = capsys.readouterr()
    assert str(INVALID_NAME.name).lower().replace('2.0', '2_0') in out
    assert not err


def test_app_valid_verbose(capsys):
    assert cli.app([str(VALID_NAME), '-v']) == 0
    out, err = capsys.readouterr()
    assert SUCC in out
    assert not err


def test_app_invalid_verbose(capsys):
    assert cli.app([str(INVALID_NAME), '-v']) == 1
    out, err = capsys.readouterr()
    assert FAIL in out
    assert not err

def test_app_valid_verbose_user(capsys):
    assert cli.app([str(VALID_NAME), '-l', 'A,B']) == 0
    out, err = capsys.readouterr()
    assert 'A' in out
    assert not err


def test_app_invalid_verbose_user(capsys):
    assert cli.app([str(INVALID_NAME), '-l', 'A,B']) == 1
    out, err = capsys.readouterr()
    assert 'B' in out
    assert not err
