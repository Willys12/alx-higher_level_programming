#!/usr/bin/python3
import importlib.util


def print_defined_names(module_name):
    spec = importlib.util.spec_from_file_location(module_name, \
            f"{module_name}.pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    for name in sorted(dir(module)):
        if not name.startswith("__"):
            print(name)


if __name__ == "__main__":
    module_name = "hidden_4"
    print_defined_names(module_name)
