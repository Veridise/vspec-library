#!/usr/bin/env python3

import argparse
import yaml
import json
from pathlib import Path

def main():
    lib_file = 'library.yaml'
    out_path = 'vspec_library.json'

    lib_file_contents = Path(lib_file).read_text()
    lib = yaml.load(lib_file_contents, Loader=yaml.CLoader)

    proc_lib = {}
    categories = lib['categories']
    proc_lib['categories'] = [cat for _, cat in lib['categories'].items()]
    for spec in lib['specs']:
        spec['category'] = categories[spec['category']]['id']
    proc_lib['specs'] = lib['specs']

    with open(out_path, 'w') as f:
        json.dump(proc_lib, f)

if __name__ == '__main__':
    main()
