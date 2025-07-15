# Publishing Apollog to PyPI

This guide explains how to publish the Apollog package to the Python Package Index (PyPI) so that users can install it using `pip install apollog`.

## Prerequisites

1. Create a PyPI account:
   - Go to https://pypi.org/account/register/
   - Follow the registration process
   - Verify your email address

2. Install required tools:
   ```bash
   pip install build twine
   ```

## Building the Distribution Packages

1. Clean previous builds (if any):
   ```bash
   rm -rf dist/ build/ *.egg-info/
   ```
   
   On Windows:
   ```bash
   rmdir /s /q dist build
   del /s /q *.egg-info
   ```

2. Build the distribution packages:
   ```bash
   python -m build
   ```
   
   Or alternatively:
   ```bash
   python setup.py sdist bdist_wheel
   ```

   This will create both source distribution (`.tar.gz`) and wheel (`.whl`) files in the `dist/` directory.

## Uploading to PyPI

### Direct Upload to PyPI

```bash
python -m twine upload dist/*
```

You'll be prompted for your PyPI username and password.

### Using API Token (More Secure)

1. Generate an API token on PyPI:
   - Go to https://pypi.org/manage/account/
   - Click on "Add API token"
   - Set the token scope (project or account-wide)
   - Copy the token

2. Use the token with twine:
   ```bash
   python -m twine upload --username __token__ --password pypi-YOUR-TOKEN-HERE dist/*
   ```

## After Publishing

Once your package is published:

1. Users can install it with:
   ```bash
   pip install apollog
   ```

2. They can then use the CLI command:
   ```bash
   apollog --help
   apollog init
   apollog deploy --config examples/config.yaml
   ```

## Updating Your Package

When you want to release a new version:

1. Update the version number in `apollog/__init__.py`
2. Rebuild and upload the new distribution packages
