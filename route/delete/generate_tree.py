import os
import fnmatch
from .default_values import *

def format_tree_line(
    name, is_dir, prefix, is_last, emoji_padding, file_emojis, directory_emojis,
    folder_emoji, module_folder_emoji, file_emoji, connector_char, default_file_name_padding
):
    """
    Formats a single line for the directory tree.
    """
    # Choose the correct tree connector: ├── for middle items, └── for last item
    connector = "└" + connector_char if is_last else "├" + connector_char

    # Determine emoji
    if is_dir:
        emoji = directory_emojis.get(name, folder_emoji)
        if name in DEFAULT_DIRECTORY_EMOJIS:
            emoji = DEFAULT_DIRECTORY_EMOJIS[name]
    else:
        emoji = file_emojis.get(name, file_emoji)
        for key in file_emojis:
            if name.startswith(key) or name.endswith(key):
                emoji = file_emojis[key]

    # Apply padding before the filename
    emoji_left_padding = ''
    emoji_right_padding = ' '
    if emoji == "":
        extra_connector = f'{default_file_name_padding}'
    else:
        extra_connector = f'{emoji_left_padding}{emoji}{emoji_right_padding}'
    
    return f"{prefix}{connector}{extra_connector}{name}{'/' if is_dir else ''}"

def generate_directory_tree(
    directory="../", prefix="", ignore_patterns=None, ignore_exact=None, file_extensions=None,
    output_file=DEFAULT_OUTPUT_FILE, is_root=True, emoji_padding=DEFAULT_EMOJI_PADDING,
    file_padding=None, directory_padding=None, root_folder_emoji=DEFAULT_ROOT_FOLDER_EMOJI,
    root_folder_padding=DEFAULT_ROOT_FOLDER_PADDING, folder_emoji=DEFAULT_FOLDER_EMOJI,
    module_folder_emoji=DEFAULT_MODULE_FOLDER_EMOJI, folder_padding=DEFAULT_FOLDER_NAME_PADDING,
    file_emoji=DEFAULT_FILE_EMOJI, file_emojis=None, directory_emojis=None,
    connector_char=DEFAULT_CONNECTOR_CHAR, default_file_name_padding=None
):
    """
    Recursively generates a directory tree listing with formatted output.
    """
    ignore_patterns = ignore_patterns or DEFAULT_IGNORE_PATTERNS.copy()
    ignore_exact = ignore_exact or DEFAULT_IGNORE_EXACT.copy()
    file_extensions = file_extensions or DEFAULT_FILE_EXTENSIONS.copy()
    file_padding = file_padding or DEFAULT_FILE_PADDING.copy()
    directory_padding = directory_padding or DEFAULT_DIRECTORY_PADDING.copy()
    file_emojis = file_emojis or DEFAULT_FILE_EMOJIS.copy()
    directory_emojis = directory_emojis or DEFAULT_DIRECTORY_EMOJIS.copy()
    default_file_name_padding = default_file_name_padding or DEFAULT_FILE_NAME_PADDING

    tree_lines = []
    
    try:
        # Separate files and directories and apply sorting rules
        items = os.listdir(directory)
        files = sorted([f for f in items if os.path.isfile(os.path.join(directory, f))])
        dirs  = sorted([d for d in items if os.path.isdir(os.path.join(directory, d))])
        entries = files + dirs  # Ensure files are listed before directories
        
        processed_entries = [(entry, os.path.join(directory, entry), os.path.isdir(os.path.join(directory, entry))) for entry in entries]

    except Exception:
        return []
    
    for idx, (entry, full_path, is_dir) in enumerate(processed_entries):
        is_last = (idx == len(processed_entries) - 1)  # Last entry in this directory?

        # Apply ignore rules
        if entry in ignore_exact or any(fnmatch.fnmatch(entry, pattern) for pattern in ignore_patterns):
            continue
        
        # Apply file extension filter
        if not is_dir and file_extensions and not any(entry.endswith(ext) for ext in file_extensions):
            continue

        # Generate formatted tree line
        tree_lines.append(
            format_tree_line(
                entry, is_dir, prefix, is_last, emoji_padding, file_emojis, directory_emojis,
                folder_emoji, module_folder_emoji, file_emoji, connector_char, default_file_name_padding
            )
        )

        # Determine the correct prefix for the next level
        new_prefix = prefix + ("    " if is_last else "│   ")

        # Recursively generate the tree for subdirectories
        if is_dir:
            tree_lines.extend(
                generate_directory_tree(
                    directory=full_path, prefix=new_prefix,
                    ignore_patterns=ignore_patterns,
                    ignore_exact=ignore_exact, file_extensions=file_extensions, output_file=output_file,
                    is_root=False, emoji_padding=emoji_padding, file_padding=file_padding,
                    directory_padding=directory_padding, root_folder_emoji=root_folder_emoji,
                    root_folder_padding=root_folder_padding, folder_emoji=folder_emoji,
                    module_folder_emoji=module_folder_emoji, folder_padding=folder_padding,
                    file_emoji=file_emoji, file_emojis=file_emojis, directory_emojis=directory_emojis,
                    connector_char=connector_char, default_file_name_padding=default_file_name_padding
                )
            )

    return tree_lines
