# V Spec Library

This contains the data for the [V] spec library, as well as a script to "compile" the
data to a single JSON file.

## Usage

1. Create a virtual env: `python3 -m venv ./.venv`
2. Activate the virtual env: `source ./.venv/bin/activate`
3. Install dependencies: `pip install -e .`
4. "Compile" the spec library: `python3 compile.py`

This will take the specs defined in `library.yaml` and "compile" them into a
`vspec_library.json` file that can be consumed by the SaaS.

TODO: make the compile command more production ready.

