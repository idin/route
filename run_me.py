if __name__ == "__main__":
    from route import directory_tree

    ignore_starts_with={}
    ignore_ends_with={'.pyc', '.egg-info', '.ipynb'}
    ignore_exact_match={'__init__.py', '__pycache__', '.git', '.idea', '.pytest_cache', '.ipynb_checkpoints', 'build', '.gitignore'}
    specific_prefixes = {
        'LICENSE': '🦀',
        '* is_module': '🚀',
        'test': '🧪',
        '* is_test_dir': '🧪',
        '* is_root': '🛸'
    }
    tree = directory_tree(
        path=".", 
        ignore_exact_match=ignore_exact_match,
        ignore_starts_with=ignore_starts_with, 
        ignore_ends_with=ignore_ends_with,
        specific_prefixes=specific_prefixes
    )
    print(tree)
