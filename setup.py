from setuptools import setup, find_packages
from route import get_post_develop_command, get_post_install_command
import os

# Define the arguments for the dir function

dir_path = os.getcwd()
ignore_ends_with={'.pyc', '.egg-info', '.ipynb'}
ignore_exact_match={'__init__.py', '__pycache__', '.git', '.idea', '.pytest_cache', '.ipynb_checkpoints', 'build', '.gitignore'}
specific_prefixes = {
    '* is_module': '🚀',
    'test': '🧪',
    '* is_test_dir': '🧪',
    '* is_root': '🛸'
}

dir_args = {
    'path': dir_path,
    'ignore_ends_with': ignore_ends_with,
    'ignore_exact_match': ignore_exact_match,
    'specific_prefixes': specific_prefixes,
    'save_to_file': True,
    'output_file': 'DIRECTORY.md'
}

post_develop_command = get_post_develop_command(dir_args=dir_args)
post_install_command = get_post_install_command(dir_args=dir_args)

# Read the contents of README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='route',
    version='2025.2.22.0',
    author='Idin K',
    author_email='python@idin.net',
    description='A Python package for generating directory trees',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/idin/route',
    packages=find_packages(include=['route', 'route.*']),
    license="Conditional Freedom License (CFL-1.0)",
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
        "install": post_install_command,
        "develop": post_develop_command,
    },
)

