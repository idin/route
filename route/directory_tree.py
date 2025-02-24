import os
from typing import Tuple, Union, Callable, Optional, Dict
from .emoji import is_emoji, pad_emoji_in_string
from .generate_get_dir_prefix import generate_get_dir_prefix
from .starts_with import starts_with, ends_with
from .markdownify import markdownify

def get_files_then_folders(
    path: str, ignore_exact_match: set[str],
    ignore_starts_with: set[str], ignore_ends_with: set[str]
) -> list[tuple[str, str]]:
    """Returns a sorted list of (entry, type) with files before folders."""
    try:
        entries = os.listdir(path)
    except PermissionError:
        return []  # Return an empty list instead of printing

    # Separate files and directories, ensuring files come first
    files = sorted([(e, 'file') for e in entries if os.path.isfile(os.path.join(path, e))])
    folders = sorted([(e, 'dir') for e in entries if os.path.isdir(os.path.join(path, e))])

    files_and_folders = files + folders  # Ensure files are listed before folders

    filtered = []
    for name, entry_type in files_and_folders:
        if name in ignore_exact_match:
            continue
        if starts_with(string=name, starts_with_set=ignore_starts_with):
            continue
        if ends_with(string=name, ends_with_set=ignore_ends_with):
            continue
        filtered.append((name, entry_type))
    return filtered

def recursive_draw_directory_tree(
    path: str, prefix: str, show_root: bool, is_root: bool, connector_padding: str, 
    get_dir_prefix: Callable[[str], str], 
    ignore_exact_match: set[str],
    ignore_starts_with: set[str], 
    ignore_ends_with: set[str],
    dir_connector: str,
    file_connector: str,
    empty_prefix: Optional[str] = "    ",
    prefix_with_pipe: Optional[str] = "│   "
) -> str:
    """Recursively generates a simple directory tree with files before folders as a string."""
    
    # Normalize path and get root name
    path = os.path.abspath(path)
    root_name = os.path.basename(path)

    tree_output = []

    if show_root and is_root:
        tree_output.append(get_dir_prefix(path) + root_name)  # Apply dir_prefix to root

    sorted_entries = get_files_then_folders(
        path=path, ignore_exact_match=ignore_exact_match,
        ignore_starts_with=ignore_starts_with, ignore_ends_with=ignore_ends_with
    )

    for index, (entry, entry_type) in enumerate(sorted_entries):
        entry_path = os.path.join(path, entry)
        is_last = index == len(sorted_entries) - 1
        extra_connector = dir_connector if entry_type == 'dir' else file_connector
        connector = ("└─" if is_last else "├─") + extra_connector

        # Apply dir_prefix only to directories
        if entry_type == 'dir':
            display_name = get_dir_prefix(entry_path) + entry
        else:
            display_name = entry
        line = prefix + connector + connector_padding + display_name
        tree_output.append(line)
        # if line is empty: raise an error
        if line.strip() == "":
            raise ValueError(f"Line is empty: {line}")

        if entry_type == 'dir':  # Use type info instead of calling os.path.isdir()
            new_prefix = prefix + (empty_prefix if is_last else prefix_with_pipe)
            tree = recursive_draw_directory_tree(
                entry_path, prefix=new_prefix, show_root=False, 
                is_root=False, connector_padding=connector_padding, 
                get_dir_prefix=get_dir_prefix,
                ignore_exact_match=ignore_exact_match,
                ignore_starts_with=ignore_starts_with, 
                ignore_ends_with=ignore_ends_with,
                dir_connector=dir_connector,
                file_connector=file_connector,
                empty_prefix=empty_prefix,
                prefix_with_pipe=prefix_with_pipe
            )
            if tree != '':
                tree_output.append(tree)

    return "\n".join(tree_output)

def directory_tree(
    path: Optional[str] = None, 
    show_root: Optional[bool] = True, 
    connector_padding: Optional[str] = ' ',
    dir_connector: Optional[str] = '─',
    file_connector: Optional[str] = '─',
    dir_prefix: Optional[str] = "📂", 
    emoji_padding: Optional[Tuple[str, str]] = ('', ' '),
    ignore: Optional[Dict[str, set]] = None,
    ignore_exact_match: Optional[set[str]] = None,
    ignore_starts_with: Optional[set[str]] = None, 
    ignore_ends_with: Optional[set[str]] = None, 
    specific_prefixes: Optional[dict[str, Union[str, Callable[[str], bool]]]] = None,
    save_to_file: Optional[bool] = False,
    output_file: Optional[str] = None,
    empty_prefix: Optional[str] = "    ",
    prefix_with_pipe: Optional[str] = "│   "
) -> str:
    """Public function to return the directory tree as a string."""
    if path is None:
        path = os.getcwd()

    if prefix_with_pipe == 'based_on_connector':
        prefix_with_pipe = '│' + " " * (2 + len(dir_connector))
    if empty_prefix == 'based_on_connector':
        empty_prefix = " " * (3 + len(dir_connector))

    if len(empty_prefix) < len(prefix_with_pipe):
        empty_prefix = empty_prefix + " " * (len(prefix_with_pipe) - len(empty_prefix))
    elif len(empty_prefix) > len(prefix_with_pipe):
        prefix_with_pipe = prefix_with_pipe + " " * (len(empty_prefix) - len(prefix_with_pipe))

    if ignore is not None:
        ignore_exact_match = ignore_exact_match or ignore.get('exact_match', set())
        ignore_starts_with = ignore_starts_with or ignore.get('starts_with', set())
        ignore_ends_with = ignore_ends_with or ignore.get('ends_with', set())
    else:
        ignore_exact_match = ignore_exact_match or set()
        ignore_starts_with = ignore_starts_with or set()
        ignore_ends_with = ignore_ends_with or set()

    specific_prefixes = specific_prefixes or {}

    dir_prefix = pad_emoji_in_string(string=dir_prefix, padding=emoji_padding)
    specific_prefixes = {
        key: pad_emoji_in_string(string=value, padding=emoji_padding) 
        for key, value in specific_prefixes.items()
    }
    get_dir_prefix = generate_get_dir_prefix(path=path, specific_prefixes=specific_prefixes, default_prefix=dir_prefix)
    
    
    tree = recursive_draw_directory_tree(
        path=path, prefix="", show_root=show_root, 
        is_root=True, connector_padding=connector_padding, 
        ignore_exact_match=ignore_exact_match,
        ignore_starts_with=ignore_starts_with, 
        ignore_ends_with=ignore_ends_with,
        get_dir_prefix=get_dir_prefix,
        dir_connector=dir_connector,
        file_connector=file_connector,
        empty_prefix=empty_prefix,
        prefix_with_pipe=prefix_with_pipe
    )
    # markdownify the tree
    if output_file is not None and output_file.lower().endswith('.md'):
        tree = markdownify(tree)
    if save_to_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(tree)
    return tree

# Example usage:
# tree_string = draw_directory_tree("path/to/directory", dir_prefix="[DIR] ")
# print(tree_string)