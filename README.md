# folder-mirror

Generate dry-run copy plans from two directory inventory listings.

Small, dependency-light Python 3 standard library utility. Original implementation and history generated for a retrospective development exercise.

## Quick start

```sh
python3 cli.py examples/input.txt --pretty
python3 -m unittest discover -p 'test*.py'
```

Pass `-` to read standard input, `--pick KEY` for one field, and `--out PATH` to save JSON.
