# Usage

## Minimal Help

```console
❯ paikalta
usage: __main__.py [-h] [-p] [-v] [-a] [-u] input_file
__main__.py: error: the following arguments are required: input_file
```

## OASIS Upstream Valid File Example

Some variations of using default, verbose, and "print" mode:

```console
❯ paikalta test/fixtures/upstream/valid/oasis_csaf_tc-csaf_2_0-2021-5-1-11.json
# return code is 0
❯ paikalta test/fixtures/upstream/valid/oasis_csaf_tc-csaf_2_0-2021-5-1-11.json -v
TRUE
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
❯ paikalta test/fixtures/upstream/invalid/OASIS_CSAF_TC-CSAF_2.0-2021-5-1-01.json -p
oasis_csaf_tc-csaf_2_0-2021-5-1-01.json
❯ paikalta test/fixtures/upstream/invalid/OASIS_CSAF_TC-CSAF_2.0-2021-5-1-01.json -p -v
oasis_csaf_tc-csaf_2_0-2021-5-1-01.json
FALSE
```

