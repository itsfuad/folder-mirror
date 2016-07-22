#!/usr/bin/env python3
"""Command-line interface for folder-mirror."""
import argparse
import json
import sys
from folder_mirror import analyze

def main(argv=None):
    parser = argparse.ArgumentParser(description='Generate dry-run copy plans from two directory inventory listings')
    parser.add_argument('path', help='Input data file, or - for standard input')
    parser.add_argument('--out', metavar='PATH', help='Write JSON to a file')
    parser.add_argument('--pick', metavar='KEY', help='Print one top-level result field')
    parser.add_argument('--pretty', action='store_true', help='Indent JSON output')
    args = parser.parse_args(argv)
    if args.path == '-':
        data = sys.stdin.read()
    else:
        with open(args.path, encoding='utf-8') as f:
            data = f.read()
    try:
        output = analyze(data)
    except (ValueError, TypeError) as error:
        parser.exit(2, 'Invalid input: ' + str(error) + '\n')
    if args.pick:
        if args.pick not in output: parser.error('Unknown output field: ' + args.pick)
        output = output[args.pick]
    rendered = json.dumps(output, sort_keys=True, indent=2 if args.pretty else None)
    if args.out:
        with open(args.out, 'w', encoding='utf-8') as target: target.write(rendered + '\n')
    else: print(rendered)
    return 0

if __name__ == '__main__':
    sys.exit(main())
