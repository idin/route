# Default configurations
DEFAULT_IGNORE_PATTERNS = [
    "*.pyc", "*.pyo", "*.egg-info", "*.log", "*.tmp", "old*", "*old.py"
]
DEFAULT_IGNORE_EXACT = [
    "__pycache__", "build", "dist", ".git", ".idea", ".vscode", "lessons", ".ipynb_checkpoints",
    "jupyter_notebooks", "data", ".pytest_cache", "__init__.py", ".gitignore"
]

# Default emoji and padding configurations
DEFAULT_EMOJI_PADDING = ' '
DEFAULT_DIRECTORY_EMOJIS = {
    "tests": "🧪",
    "test": "🧪",
    "route": "🛸"
}
DEFAULT_FILE_EMOJIS = {
    "setup.py": "🐍",
    "test_": "",
    ".py": "",
    "README.md": "📜",
    "DIRECTORY_TREE.md": "📜",
    "LICENSE": "🦀"
}
DEFAULT_DIRECTORY_PADDING = {}
DEFAULT_FILE_PADDING = {
    "test_": "~",
}

# Default file extensions to be shown in the tree
DEFAULT_FILE_EXTENSIONS = ['.md', '', '.py']

# Default emoji constants
DEFAULT_ROOT_FOLDER_EMOJI = "🚗"
DEFAULT_FOLDER_EMOJI = "📂"
DEFAULT_MODULE_FOLDER_EMOJI = "🚀"
DEFAULT_TEST_FOLDER_EMOJI = "🧪"
DEFAULT_FILE_EMOJI = ""

# Customization for tree formatting
DEFAULT_CONNECTOR_CHAR = "─"
DEFAULT_FOLDER_NAME_PADDING = " "
DEFAULT_FILE_NAME_PADDING = "── "  # length should be 3
#DEFAULT_FILE_NAME_PADDING = "1234"
assert len(DEFAULT_FILE_NAME_PADDING) == 3
DEFAULT_ROOT_FOLDER_PADDING = ""

# Default output file for markdown
DEFAULT_OUTPUT_FILE = 'DIRECTORY_TREE.md'
