#!/usr/bin/env bash
read -p "Warning: This will delete the broken-down library and recreate it from the yaml file. Hit Ctrl+Break to stop if this is not what you expect!"
rm -rm library
./breakdown.py
./compile.py
cat vspec_library_old.json | sed 's/"category": 0/"category": "erc20"/g' | sed 's/"category": 1/"category": "erc721"/g' | sed 's/"category": 2/"category": "erc3156"/g' | jq > nx.old
cat vspec_library.json| jq > nx.new
meld nx.old nx.new
rm nx.old nx.new

