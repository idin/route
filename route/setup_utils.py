import subprocess
from setuptools.command.install import install
from setuptools.command.develop import develop
import importlib
from .directory_tree import directory_tree
import os

class PostInstallCommand(install):
    """Post-installation command to run the dir function after install."""
    def __init__(self, *args, **kwargs):
        self.dir_args = kwargs.pop('dir_args', {})
        super().__init__(*args, **kwargs)

    def run(self):
        install.run(self)  # Run the standard install process
        print("Running dir function from route package after installation...")
        try:
            # Use the provided directory arguments
            directory_tree(**self.dir_args)
            print("Successfully ran dir function")
        except Exception as e:
            print(f"Error running dir function: {e}")
            raise e

class PostDevelopCommand(develop):
    """Post-installation command for editable installs."""
    def __init__(self, *args, **kwargs):
        self.dir_args = kwargs.pop('dir_args', {})
        super().__init__(*args, **kwargs)

    def run(self):
        develop.run(self)  # Run the standard develop process
        print("Running dir function from route package after editable install...")
        try:
            # Use the provided directory arguments
            dir(**self.dir_args)
            print("Successfully ran dir function")
        except Exception as e:
            print(f"Error running dir function: {e}")
            raise e

def configure_post_install(module_name, function_name):
    """Configure the module and function for post-installation commands."""
    PostInstallCommand.module_name = module_name
    PostInstallCommand.function_name = function_name
    PostDevelopCommand.module_name = module_name
    PostDevelopCommand.function_name = function_name 

def get_post_install_command(dir_args=None):
    """
    This function gets the inputs for dir function and produces a post install command.
    """
    class CustomPostInstallCommand(PostInstallCommand):
        def __init__(self, *args, **kwargs):
            kwargs['dir_args'] = dir_args or {}
            super().__init__(*args, **kwargs)
    return CustomPostInstallCommand

def get_post_develop_command(dir_args=None):
    """
    This function gets the inputs for dir function and produces a post develop command.
    """
    class CustomPostDevelopCommand(PostDevelopCommand):
        def __init__(self, *args, **kwargs):
            kwargs['dir_args'] = dir_args or {}
            super().__init__(*args, **kwargs)
    return CustomPostDevelopCommand
