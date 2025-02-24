# Route 🧭

Route is a Python package for generating directory tree, especially in any python project or package.

## Installation

```bash
pip install route
```

## Usage



```python
from route import directory_tree

directory_tree(path=".", save_to_file=True, display_output=True)
```

Output:
```
🛸 route
├── README.md
├── run_me.py
├── setup.py
└── 🚀 route
    ├── dir.py
    ├── directory_tree.py
    ├── emoji.py
    ├── generate_get_dir_prefix.py
    ├── setup_utils.py
    └── starts_with.py
```


## How to Use Route in Your Python Package

- Use the following code at the top of your `setup.py` file (Script 1)
- Add `post_install_command` and `post_develop_command` to the `cmdclass` argument in the `setup` function (Script 2)
- See the [`setup.py`](setup.py) file for an example.

### Script 1
```python
from route import get_post_develop_command, get_post_install_command
import os

# Define the arguments for the dir function
dir_path = os.getcwd()
ignore_ends_with={'.pyc', '.egg-info', '.ipynb'}
ignore_exact_match={
    '__init__.py', '__pycache__', '.git', '.idea', '.pytest_cache', '.ipynb_checkpoints', 
    'dist', 'build', '.gitignore'
}
specific_prefixes = {
    '* is_root': '🛸',
    '* is_module': '🚀',
    '* is_test_dir': '🧪',
    'test': '🧪',
    'tests': '🧪'
}

dir_args = {
    'path': dir_path,
    'ignore_ends_with': ignore_ends_with,
    'ignore_exact_match': ignore_exact_match,
    'specific_prefixes': specific_prefixes,
    'save_to_file': True,           # This creates a Markdown file
    'output_file': 'DIRECTORY.md'   # This is the name of the file that will be created
}

post_develop_command = get_post_develop_command(dir_args=dir_args)
post_install_command = get_post_install_command(dir_args=dir_args)
```

### Script 2
```python
setup(
    ...
    cmdclass={
        "install": post_install_command,
        "develop": post_develop_command,
    },
    ...
)
```









