# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pathlib
import sys
import pytest  # type: ignore

import csaf_parser.tmp as cli_legacy
import csaf_parser.cli as cli


def test_main_nok_empty_(capsys):
    with pytest.raises(SystemExit):
        cli_legacy.main([])
    out, err = capsys.readouterr()
    for term in ('file', 'required'):
        assert term in err


def test_main_nok_int_(capsys):
    with pytest.raises(TypeError):
        cli_legacy.main(42)
    out, err = capsys.readouterr()
    assert not out
    assert not err


def test_main_nok_ints_(capsys):
    sequence_of_ints = [1, 2, 3]
    with pytest.raises(TypeError):
        cli_legacy.main(sequence_of_ints)
    out, err = capsys.readouterr()
    assert not out
    assert not err


def test_main_nok_non_existing_folder_(capsys):
    nef = non_existing_folder_path = 'folder_does_not_exist'
    a_name = 'my_script'
    assert pathlib.Path(nef).is_dir() is False, f"Unexpected folder {nef} exists which breaks this test"
    message = '%s: I/O error: "%s" does not exist' % (a_name, nef)
    sys.argv.append('--file')
    sys.argv.append(nef)
    with pytest.raises(SystemExit, match=message):
        cli_legacy.main(a_name)
    out, err = capsys.readouterr()


def test_main_nok_empty():
    assert cli.main([]) is None


def test_main_nok_int(capsys):
    assert cli.main([42]) is None
    out, err = capsys.readouterr()
    assert not out
    assert not err
