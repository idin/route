# Route 🚗

## Setup Utilities

This package includes a utility module `setup_utils.py` that provides post-installation hooks for your Python package. These hooks allow you to run a specific function from a module automatically after the package is installed or when it is installed in editable mode.

### How to Use

1. **Import the Utility Module**: In your `setup.py` file, import the `PostInstallCommand` and `PostDevelopCommand` classes from `setup_utils.py`.

    ```python
    from route.setup_utils import PostInstallCommand, PostDevelopCommand
    ```

2. **Set the Module and Function**: Specify the module and function you want to run after installation by setting the `module_name` and `function_name` attributes for both `PostInstallCommand` and `PostDevelopCommand`.

    ```python
    PostInstallCommand.module_name = "route.dir"
    PostInstallCommand.function_name = "generate_tree_structure"
    PostDevelopCommand.module_name = "route.dir"
    PostDevelopCommand.function_name = "generate_tree_structure"
    ```

3. **Configure `setup.py`**: Use these classes in the `cmdclass` argument of the `setup()` function in your `setup.py`.

    ```python
    setup(
        # ... other setup arguments ...
        cmdclass={
            "install": PostInstallCommand,  # Runs function after standard install
            "develop": PostDevelopCommand,  # Runs function after editable install (-e)
        },
        # ... other setup arguments ...
    )
    ```

### Example

Here is an example of how your `setup.py` might look:

```python
from setuptools import setup, find_packages
from route.setup_utils import PostInstallCommand, PostDevelopCommand

# Read the contents of README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Set the module and function for post-installation commands
PostInstallCommand.module_name = "route.dir"
PostInstallCommand.function_name = "generate_tree_structure"
PostDevelopCommand.module_name = "route.dir"
PostDevelopCommand.function_name = "generate_tree_structure"

setup(
    name='your_package_name',
    version='0.1.0',
    author='Your Name',
    author_email='your_email@example.com',
    description='A description of your package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/yourrepository',
    packages=find_packages(),
    license="Your License",
    install_requires=[
        'plotly>=5.0.0',
        'pandas>=2.0.0',
        'numpy>=1.23.5',
        'openai>=1.0.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Your License',
        'Operating System :: OS Independent',
    ],
    cmdclass={
        "install": PostInstallCommand,  # Runs function after standard install
        "develop": PostDevelopCommand,  # Runs function after editable install (-e)
    },
    python_requires='>=3.6',
)
```

## Usage Example

To use the `dir` function from the `route` package, you can create a script like `example_usage.py`:

```python
from route import dir

# Use the dir function to generate a directory tree
dir(
    directory="path/to/directory", 
    save_to_file=True, 
    display_output=True
)
```

Run this script to generate a directory tree for the specified path.