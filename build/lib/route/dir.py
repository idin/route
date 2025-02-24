from .generate_tree import generate_directory_tree
from .default_values import *

def dir(
    directory="../",
    ignore_patterns=None,
    ignore_exact=None,
    file_extensions=None,
    save_to_file=False,
    display_output=True,
    output_file=DEFAULT_OUTPUT_FILE,
    emoji_padding=DEFAULT_EMOJI_PADDING,
    file_padding=None,
    directory_padding=None,
    root_folder_emoji=DEFAULT_ROOT_FOLDER_EMOJI,
    root_folder_padding=DEFAULT_ROOT_FOLDER_PADDING,
    folder_emoji=DEFAULT_FOLDER_EMOJI,
    folder_padding=DEFAULT_FOLDER_NAME_PADDING,
    file_emoji=DEFAULT_FILE_EMOJI,
    file_emojis=None,
    directory_emojis=None,
    connector_char=DEFAULT_CONNECTOR_CHAR,
    default_file_name_padding=None
):
    """
    Generates a tree structure of the given directory with sorting and filtering options.

    Args:
        directory (str): The directory to generate the tree for.
        ignore_patterns (list): Patterns to ignore.
        ignore_exact (list): Exact names to ignore.
        file_extensions (list): File extensions to include.
        save_to_file (bool): Whether to save the output to a file.
        display_output (bool): Whether to display the output.
        output_file (str): The file to save the output to.
        emoji_padding (str): Padding for emojis.
        file_padding (dict): Padding for files.
        directory_padding (dict): Padding for directories.
        root_folder_emoji (str): Emoji for the root folder.
        root_folder_padding (str): Padding for the root folder.
        folder_emoji (str): Emoji for folders.
        folder_padding (str): Padding for folder names.
        file_emoji (str): Emoji for files.
        file_emojis (dict): Emojis for specific files.
        directory_emojis (dict): Emojis for specific directories.
        connector_char (str): Character for tree connectors.
        default_file_name_padding (str): Default padding for file names.

    Returns:
        list: The generated tree structure as a list of strings.
    """
    ignore_patterns = ignore_patterns or DEFAULT_IGNORE_PATTERNS.copy()
    ignore_exact = ignore_exact or DEFAULT_IGNORE_EXACT.copy()
    file_extensions = file_extensions or DEFAULT_FILE_EXTENSIONS.copy()
    file_padding = file_padding or DEFAULT_FILE_PADDING.copy()
    directory_padding = directory_padding or DEFAULT_DIRECTORY_PADDING.copy()
    file_emojis = file_emojis or DEFAULT_FILE_EMOJIS.copy()
    directory_emojis = directory_emojis or DEFAULT_DIRECTORY_EMOJIS.copy()
    default_file_name_padding = default_file_name_padding or DEFAULT_FILE_NAME_PADDING

    tree_output = generate_directory_tree(
        directory=directory,
        ignore_patterns=ignore_patterns,
        ignore_exact=ignore_exact,
        file_extensions=file_extensions,
        output_file=output_file,
        is_root=True,
        emoji_padding=emoji_padding,
        file_padding=file_padding,
        directory_padding=directory_padding,
        root_folder_emoji=root_folder_emoji,
        root_folder_padding=root_folder_padding,
        folder_emoji=folder_emoji,
        folder_padding=folder_padding,
        file_emoji=file_emoji,
        file_emojis=file_emojis,
        directory_emojis=directory_emojis,
        connector_char=connector_char,
        default_file_name_padding=default_file_name_padding
    )

    if save_to_file and output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("## Project Directory Structure\n\n````java\n\n" + "\n".join(tree_output) + "\n````\n")

    if display_output:
        print("\n".join(tree_output))


def main():
    """Runs the tree generator as a script or CLI command."""
    global DEFAULT_OUTPUT_FILE
    directory = "../route"  # Default to atlantis if no argument is provided

    if len(sys.argv) > 1:
        directory = sys.argv[1]
    if len(sys.argv) > 2:
        DEFAULT_OUTPUT_FILE = sys.argv[2] if sys.argv[2].endswith(".md") else None

    ignore_patterns = DEFAULT_IGNORE_PATTERNS.copy()
    ignore_exact = DEFAULT_IGNORE_EXACT.copy()
    file_extensions = DEFAULT_FILE_EXTENSIONS.copy()

    for arg in sys.argv[3:]:
        if arg.startswith("--ext="):
            file_extensions = arg[6:].split(",")

    dir(
        directory=directory,
        ignore_patterns=ignore_patterns,
        ignore_exact=ignore_exact,
        file_extensions=file_extensions,
        save_to_file=bool(DEFAULT_OUTPUT_FILE),
        display_output=True,
        output_file=DEFAULT_OUTPUT_FILE
    )


if __name__ == "__main__":
    main()