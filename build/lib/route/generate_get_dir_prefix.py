from typing import Callable, Union
import os

def dir_is_module(path: str) -> bool:
    return os.path.exists(os.path.join(path, "__init__.py"))

def dir_is_test(path: str) -> bool:
    # if the majority of the files in the directory are test files, return True
    test_files = ["test", "tests", "test_", "test_", "test.", "test-", "test_"]
    files = os.listdir(path)
    test_files = [file for file in files if any(file.startswith(test_file) for test_file in test_files)]
    return len(test_files) > len(files) / 2

def generate_get_dir_prefix(
    path: str,
    specific_prefixes: dict[str, Union[str, Callable[[str], bool]]], 
    default_prefix: str
) -> Callable[[str], str]:
    """
    specific_prefixes is a dictionary that contains two types keys:
    - keys that start with *
    - keys that don't start with *

    if a key starts with *, it is pointing to a function that should be called on dir and if True, the value of the key should be used as a prefix
    if a key doesn't start with *, if the dir name is the key, the prefix is the value of the key
    """
    def dir_is_root(_path: str) -> bool:
        return os.path.abspath(_path) == os.path.abspath(path)

    functions = {
        'is_module': dir_is_module,
        'is_test_dir': dir_is_test,
        'is_root': dir_is_root,
    }

    def get_dir_prefix(path: str) -> str:
        if path == 'atlantis':
            raise
        dir_name = os.path.basename(path)
        if dir_name in specific_prefixes:
            return specific_prefixes[dir_name]
        for key in specific_prefixes:
            if key.startswith("*"):
                clean_key = key.strip("*").strip()
                function = functions[clean_key]
                if function(path):
                    return specific_prefixes[key]
        return default_prefix

    return get_dir_prefix