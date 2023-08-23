#!/usr/bin/env python3
import os
import re
from pathlib import Path
import yaml
from utils import write_json, write_file

LIB_FILE = "library.yaml"
OUT_PATH = "library"
fix_prefix = re.compile(r"^[1-9]\..*")


def category_path(category_code: str):
    return os.path.join(OUT_PATH, category_code)


def category_metadata_path(category_code: str):
    return os.path.join(category_path(category_code), ".category_metadata.json")


def spec_path(category_code: str, spec_name: str):
    if fix_prefix.match(spec_name):
        spec_name = "0" + spec_name
    return os.path.join(category_path(category_code), spec_name) + ".spec"


def spec_metadata_path(category_code: str, spec_name: str):
    return spec_path(category_code, spec_name) + ".json"


def main():
    lib_file_contents = Path(LIB_FILE).read_text()
    lib = yaml.load(lib_file_contents, Loader=yaml.CLoader)

    categories = lib["categories"]
    for code, metadata in categories.items():
        print("Category:", code, "path:", category_path(code), "metadata:", metadata)
        os.makedirs(category_path(code), exist_ok=True)
        write_json(
            category_metadata_path(code),
            {k: metadata[k] for k in metadata.keys() if k not in ["id", "category"]}
            | {"view_order": metadata["id"]},
        )

    # proc_lib['categories'] = [cat for _, cat in lib['categories'].items()]
    for spec in lib["specs"]:
        category_code = spec["category"]
        if category_code not in categories:
            print(f"ERROR: category {category_code} does not exist")
            exit(1)
        # spec["category"] = categories[spec["category"]]["id"]
        print("Spec:", spec_path(category_code, spec["name"]))
        write_file(spec_path(category_code, spec["name"]), spec["spec"])
        if "desc" in spec:
            if "\n" in spec["desc"]:
                print("Removing newline from:", spec["desc"])
                spec["desc"] = spec["desc"].replace("\n", " ").strip()

        write_json(
            spec_metadata_path(category_code, spec["name"]),
            {k: spec[k] for k in spec if k not in ["name", "spec", "category"]},
        )


if __name__ == "__main__":
    main()
