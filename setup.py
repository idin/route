"""
I am dogfooding the route package by using it to set up its own environment and manage its directory structure.
"""
from route import get_post_develop_command, get_post_install_command
import os

# Define the arguments for the dir function

dir_args = {
    'path': os.getcwd(),
    'ignore': {
        'exact_match': {
            '__init__.py', '__pycache__', '.git', '.idea', '.pytest_cache', 
            '.ipynb_checkpoints', 'dist', 'build', '.gitignore'
        },
        'ends_with': {'.pyc', '.egg-info', '.ipynb', '.whl'}
    },
    'specific_prefixes': {
        '* is_root': '🛸',
        '* is_module': '🚀',
        '* is_test_dir': '🧪',
        'test': '🧪',
        'tests': '🧪'
    },
    'save_to_file': True,           # This creates a Markdown file
    'output_file': 'DIRECTORY.md'   # This is the name of the file that will be created
}

post_develop_command = get_post_develop_command(dir_args)
post_install_command = get_post_install_command(dir_args)

"""
The following is the setup.py file for the route package.
"""

from setuptools import setup, find_packages
import os

# Read the contents of README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='route',
    version='2025.2.23.1',
    author='Idin K',
    author_email='python@idin.net',
    description='A Python package for generating directory trees',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/idin/route',
    packages=find_packages(include=['route', 'route.*']),
    license="Conditional Freedom License (CFL-1.0)",
    license_files='LICENSE',
    install_requires=[
        # List any dependencies your package needs
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in
    cmdclass={
        "install": post_install_command, # This creates the DIRECTORY.md file
        "develop": post_develop_command, # This creates the DIRECTORY.md file
    },
)

