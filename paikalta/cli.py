"""From the place (Finnish: paikalta) we derive the name - command line interface."""
import argparse
import json
import pathlib
import re
import sys
from typing import List, no_type_check

import paikalta.api as api
from paikalta import (
    APP_NAME,
    APP_VERSION,
    ENCODING,
    FAIL,
    INVALID_ID,
    LOG_SEPARATOR,
    QUIET,
    SUCC,
    TS_FORMAT_PAYLOADS,
    VALID_NAME_PAT,
    log,
)


@no_type_check
def parser():
    """Implementation of command line API returning parser."""
    impl = argparse.ArgumentParser(description='Verifies or modifies the name of a CSAF 2.0 advisory file')
    impl.add_argument('input_file', type=str, help='CSAF advisory file to verify or modify the filename of')
    impl.add_argument('-p', '--print', dest='echo', action='store_true', help='Prints the correct filename')
    impl.add_argument(
        '-l',
        '--labels',
        dest='labels',
        type=str,
        help='Comma separate pair of SUCC,FAIL labels (in that order) activating verbose mode',
    )
    impl.add_argument(
        '-v',
        '--verbose',
        dest='verbose',
        action='store_true',
        help=f'Prints the logic result as either {SUCC} or {FAIL} if not overridden by --label option',
    )
    impl.add_argument(
        '-a',
        '--add',
        dest='add',
        action='store_true',
        help=(
            'Writes the CSAF advisory file to the correct filename if different'
            ' - will overrule -u/--update if given in addition'
        ),
    )
    impl.add_argument(
        '-u',
        '--update',
        dest='update',
        action='store_true',
        help=(
            'Renames the CSAF advisory file to the correct filename if necessary'
            ' - will be overruled by -a/--add if given in addition'
        ),
    )
    return impl


@no_type_check
def app(argv=None):
    """Drive the verification or modification of advisory file(name)s per CSAF 2.0 rules."""
    argv = sys.argv[1:] if argv is None else argv
    options = parser().parse_args(argv)
    return api.process(options)


if __name__ == '__main__':
    sys.exit(app(sys.argv[1:]))
