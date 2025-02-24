from setuptools import setup, find_packages

# Read the contents of README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='example_package',  # This is the name of the user's package
    version='0.1.0',
    author='Example Author',
    author_email='example_author@example.com',
    description='An example package demonstrating the use of the route package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/example_author/example_package',
    packages=find_packages(),
    install_requires=[
        'route>=2025.2.22.0',  # Specify your package as a dependency
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

# Example usage of the dir function from the route package
if __name__ == "__main__":
    from route import dir

    # Use the dir function to generate a directory tree
    dir(
        directory="C:/path/to/valid/directory",  # Ensure this is a valid path
        save_to_file=True, 
        display_output=True
    ) 