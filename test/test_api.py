import pathlib

import pytest

import paikalta.api as api

from paikalta import INVALID_ID


def test_compute_filename():
    data = {'document': {'tracking': {'id': 'foo'}}}
    assert api.compute_filename(data) == 'foo.json'


def test_compute_filename_missing():
    data = {'document': {'tracking': {'id': ''}}}
    assert api.compute_filename(data) == f'{INVALID_ID}.json'


def test_dump_load(tmp_path):
    data = {'document': {'tracking': {'id': 'foo'}}}
    name = api.compute_filename(data)
    api.dump(data, pathlib.Path(tmp_path / name))
    assert len(list(tmp_path.iterdir())) == 1
    reload = api.load(tmp_path / name)
    assert reload == data


def test_dump_fail():
    data = {'document': {'tracking': {'id': 'foo'}}}
    name = api.compute_filename(data)
    message = rf"\[Errno 20\] Not a directory: '/dev/null/{name}'"
    with pytest.raises(NotADirectoryError, match=message):
        api.dump(data, pathlib.Path(f'/dev/null/{name}'))
