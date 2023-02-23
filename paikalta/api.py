"""From the place (Finnish: paikalta) we derive the name - application programming interface."""
import argparse
import pathlib
import re
import sys
from typing import List, Union, no_type_check

import msgspec
from paikalta import (
    APP_NAME,
    APP_VERSION,
    COMMA,
    ENCODING,
    FAIL,
    INVALID_ID,
    LOG_SEPARATOR,
    QUIET,
    SUCC,
    TS_FORMAT_PAYLOADS,
    VALID_NAME_PAT,
    parse_csl_as_is,
    log,
)


@no_type_check
def load(csaf_path):
    """Load the CSAF data from the path to the JSON file or fail miserably."""
    with open(csaf_path, 'rt', encoding=ENCODING) as handle:
        return msgspec.json.decode(handle.read())


@no_type_check
def dump(csaf_data, csaf_path):
    """Dump the CSAF data formatted to 2 space indent to the JSON file given by the path."""
    with open(csaf_path, 'wt', encoding=ENCODING) as f:
        f.write(msgspec.json.format(msgspec.json.encode(csaf_data)).decode())


@no_type_check
def compute_filename(csaf_data):
    """Derive the filename from document/tracking/id if exists else return the conventional invalid json name."""
    document_tracking_id = INVALID_ID
    if (doc := csaf_data.get('document')) and (track := doc.get('tracking')) and (the_id := track.get('id')):  # noqa
        document_tracking_id = the_id

    return f'{re.sub(VALID_NAME_PAT, "_", document_tracking_id.lower())}.json'


@no_type_check
def derive(pointer: Union[str, dict[str, object], pathlib.Path]) -> str:
    """Derive the filename from data else return the conventional invalid json name."""
    return compute_filename(load(pointer) if isinstance(pointer, (str, pathlib.Path)) else pointer)


@no_type_check
def filename_is_valid(path: Union[str, pathlib.Path], data: Union[None, dict[str, object]] = None) -> bool:
    """Verify the filename from data matches the given (True) else return False."""
    given = pathlib.Path(path).name
    data = load(path) if data is None else data
    derived = compute_filename(data)
    return derived == given


@no_type_check
def process(options: argparse.Namespace):
    """Process the command line request."""
    if options.labels:
        options.verbose = True
    succ, fail = SUCC, FAIL
    if options.labels and COMMA in options.labels:
        succ, fail = parse_csl_as_is(options.labels)

    data = load(options.input_file)
    current_path = pathlib.Path(options.input_file)
    correct_path = current_path.parent / compute_filename(data)
    ok = current_path == correct_path

    if options.echo:
        print(correct_path.name)
    if options.verbose:
        print(succ if ok else fail)

    if ok:
        return 0

    if options.add:
        dump(data, correct_path)
    elif options.update:
        _ = current_path.rename(correct_path)

    return 1
