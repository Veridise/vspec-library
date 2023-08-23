#!/usr/bin/env python3

import os
from utils import read_json, write_json, read_file


def main():
    SPEC_EXTENSION = ".spec"
    in_path = os.path.join(os.getcwd(), "library")
    library = {"categories": [], "specs": []}

    print("Reading categories...")
    for category in [
        e for e in os.listdir(in_path) if os.path.isdir(os.path.join(in_path, e))
    ]:
        print("Category:", category)
        category_root = os.path.join(in_path, category)
        try:
            category_metadata = read_json(
                os.path.join(category_root, ".category_metadata.json")
            )
        except Exception as ex:
            raise Exception(  # pylint: disable=broad-exception-raised
                f"Error reading metadata for category {category} "
            ) from ex
        library["categories"].append({"id": category} | category_metadata)

    library["categories"].sort(key=lambda e: e["view_order"])

    for category in [e["id"] for e in library["categories"]]:
        category_root = os.path.join(in_path, category)
        for spec_file in sorted(
            [e for e in os.listdir(category_root) if e.endswith(SPEC_EXTENSION)]
        ):
            spec_data = read_file(os.path.join(category_root, spec_file))
            spec_metadata = read_json(os.path.join(category_root, f"{spec_file}.json"))
            spec_entry = spec_metadata | {
                "category": category,
                "name": spec_file[0 : 0 - len(SPEC_EXTENSION)],
                "spec": spec_data,
            }
            library["specs"].append(spec_entry)

    write_json("vspec_library.json", library)
    print("Done")


if __name__ == "__main__":
    main()
