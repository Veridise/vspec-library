# V Spec Library

This contains the data for the [V] spec library, as well as a script to "compile" the
data to a single JSON file.

## Usage

1. Create a virtual env: `python3 -m venv ./.venv`
2. Activate the virtual env: `source ./.venv/bin/activate`
3. Install dependencies: `pip install -e .`
4. "Compile" the spec library: `python3 compile.py`
5. "Release" a version of the library: `./release.sh <version>`. The new version is maintained in file `vpesc_library.latest`. Note that this process indirectly invokes `compile.py`
6. "Deploy" the latest version of the library to one of our environments: `./deploy.sh <env>`, where env is either `dev` or `internal`

The workflow is to edit specs and metadata inside the `library` directory, and invoke `compile.py` to verify things are working. When ready, call `release.sh` to make a new named release, and then call `deploy.sh` to upload the latest produced version to one of the SaaS deployments for consumption. 

## TODO 
    1. make the compile command more production ready by:
        a. checking the metadata format against a Pydantic model
        b. syntax-checking the individual spec files using an actual V parser.
