# API

```python
>>> import paikalta.api as api
>>> api.filename_is_valid('test/fixtures/upstream/valid/oasis_csaf_tc-csaf_2_0-2021-5-1-11.json')
True
>>> api.filename_is_valid('file-nowhere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/some/where/paikalta/api.py", line 58, in filename_is_valid
    data = load(path) if data is None else data
  File "/some/where/paikalta/api.py", line 27, in load
    with open(csaf_path, 'rt', encoding=ENCODING) as handle:
FileNotFoundError: [Errno 2] No such file or directory: 'file-nowhere'
>>> api.derive('test/fixtures/upstream/valid/oasis_csaf_tc-csaf_2_0-2021-5-1-11.json')
'oasis_csaf_tc-csaf_2_0-2021-5-1-11.json'
>>> data = api.load('test/fixtures/upstream/valid/oasis_csaf_tc-csaf_2_0-2021-5-1-11.json')
>>> api.filename_is_valid('test/fixtures/upstream/valid/oasis_csaf_tc-csaf_2_0-2021-5-1-11.json', data)
True
>>> api.filename_is_valid('oasis_csaf_tc-csaf_2_0-2021-5-1-11.json', data)
True
```
