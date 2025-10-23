#!/bin/bash

set -x

uv run ./from-json.py --input testdata/f4.jsonl > actual/from-json-1
uv run ./from-json.py < testdata/f4.jsonl > actual/from-json-2

uv run ./to-table-format.py --input testdata/f1 --format github > actual/to-table-format-1
uv run ./to-table-format.py < testdata/f2 > actual/to-table-format-2

uv run ./sort.py --input testdata/f1 --column col1 --direction desc > actual/sort-1
uv run ./sort.py --column col5 --direction asc <  testdata/f3 > actual/sort-2

uv run ./rename-columns.py --input testdata/f2 --column col1,new_col1 > actual/rename-1
uv run ./rename-columns.py --input testdata/f2 --column col1,new_col1 --column col3,new_col3 > actual/rename-2
uv run ./rename-columns.py --column col3,new_col3 < testdata/f2 > actual/rename-3

uv run ./query.py --input testdata/f1 --query 'col1 == "g"' > actual/query-1
uv run ./query.py --query 'col2 > 3' < testdata/f1 > actual/query-2

uv run ./pluck.py --input testdata/f2 --column col1 > actual/pluck-1
uv run ./pluck.py --input testdata/f2 --column col1 --column col3 > actual/pluck-2
uv run ./pluck.py --column col1 < testdata/f2 > actual/pluck-3

uv run ./join.py testdata/f1 testdata/f2 > actual/join-1
uv run ./join.py --input testdata/f1 testdata/f2 > actual/join-2
uv run ./join.py < testdata/f1 > actual/join-3

uv run ./concat.py testdata/f1 testdata/f2 > actual/concat-1
uv run ./concat.py --input testdata/f1 testdata/f2 > actual/concat-2
uv run ./concat.py < testdata/f1 > actual/concat-3
uv run ./concat.py --direction h testdata/f1 testdata/f2 > actual/concat-d-1

uv run ./drop-columns.py --input testdata/f2 --column col1 > actual/drop-colums-1
uv run ./drop-columns.py --input testdata/f2 --column col1 --column col4 > actual/drop-colums-2
uv run ./drop-columns.py --column col1 < testdata/f2 > actual/drop-colums-3

diff -r --exclude=.gitignore expected actual
