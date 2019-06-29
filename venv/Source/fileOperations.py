import importlib
import magic


def get_files(filenames):
    for i in filenames:
        print(magic.from_file(i))
