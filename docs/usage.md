# Usage

## Minimal Help

```console
❯ paikalta
usage: __main__.py [-h] [-p] [-l LABELS] [-v] [-a] [-u] input_file
__main__.py: error: the following arguments are required: input_file
```

or long form:

```console
❯ paikalta -h
usage: __main__.py [-h] [-p] [-l LABELS] [-v] [-a] [-u] input_file

Verifies or modifies the name of a CSAF 2.0 advisory file

positional arguments:
  input_file            CSAF advisory file to verify or modify the filename of

options:
  -h, --help            show this help message and exit
  -p, --print           Prints the correct filename
  -l LABELS, --labels LABELS
                        Comma separate pair of SUCC,FAIL labels (in that order) activating verbose mode
  -v, --verbose         Prints the logic result as either TRUE or FALSE if not overridden by --label option
  -a, --add             Writes the CSAF advisory file to the correct filename if different - will overrule -u/--update if given in addition
  -u, --update          Renames the CSAF advisory file to the correct filename if necessary - will be overruled by -a/--add if given in addition
```

## OASIS Upstream Valid File Example

Some variations of using default, verbose, and "print" mode:

```console
❯ paikalta test/fixtures/upstream/valid/oasis_csaf_tc-csaf_2_0-2021-5-1-11.json
# return code is 0
❯ paikalta test/fixtures/upstream/valid/oasis_csaf_tc-csaf_2_0-2021-5-1-11.json -v
TRUE
❯ paikalta -l A,B -v test/fixtures/upstream/valid/oasis_csaf_tc-csaf_2_0-2021-5-1-11.json
A
❯ PAIKALTA_SUCC=YES paikalta -v test/fixtures/upstream/valid/oasis_csaf_tc-csaf_2_0-2021-5-1-11.json
YES
❯ paikalta test/fixtures/upstream/valid/oasis_csaf_tc-csaf_2_0-2021-5-1-11.json -p
oasis_csaf_tc-csaf_2_0-2021-5-1-11.json
❯ paikalta test/fixtures/upstream/valid/oasis_csaf_tc-csaf_2_0-2021-5-1-11.json -p -v
oasis_csaf_tc-csaf_2_0-2021-5-1-11.json
TRUE
```

## OASIS Upstream Invalid File Example

Some variations of using default, verbose, and "print" mode:

```console
❯ paikalta test/fixtures/upstream/invalid/OASIS_CSAF_TC-CSAF_2.0-2021-5-1-01.json
# return code is 1
❯ paikalta test/fixtures/upstream/invalid/OASIS_CSAF_TC-CSAF_2.0-2021-5-1-01.json -v
FALSE
❯ paikalta -l A,B test/fixtures/upstream/invalid/OASIS_CSAF_TC-CSAF_2.0-2021-5-1-01.json
B
❯ paikalta test/fixtures/upstream/invalid/OASIS_CSAF_TC-CSAF_2.0-2021-5-1-01.json -p
oasis_csaf_tc-csaf_2_0-2021-5-1-01.json
❯ paikalta test/fixtures/upstream/invalid/OASIS_CSAF_TC-CSAF_2.0-2021-5-1-01.json -p -v
oasis_csaf_tc-csaf_2_0-2021-5-1-01.json
FALSE
```

