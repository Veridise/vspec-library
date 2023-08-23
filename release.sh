#!/usr/bin/env bash
set -e
if [ -z "$1" ]; then
    echo "Must specify version as the first parameter"
    exit 1
fi

if [ ! -x ./compile.py ]; then
    echo "Can't find ./compile.py"
    exit 1
fi

./compile.py
mv vspec_library.json "vspec_library_$1.json"
echo "$1" > vspec_library.latest
