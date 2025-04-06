#!/bin/bash
set -e

# Clean up previous builds
rm -rf dist/ build/ *.egg-info

# Build the package
echo "Building package..."
python -m build

# Check the distribution
echo "Checking distribution..."
twine check dist/*

# Upload to Test PyPI first (optional)
echo "Do you want to upload to Test PyPI? (y/n)"
read test_upload
if [ "$test_upload" = "y" ]; then
    echo "Uploading to Test PyPI..."
    twine upload --repository testpypi dist/*
    
    echo "Testing installation from Test PyPI..."
    pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ env_loader
fi

# Upload to PyPI
echo "Do you want to upload to PyPI? (y/n)"
read pypi_upload
if [ "$pypi_upload" = "y" ]; then
    echo "Uploading to PyPI..."
    twine upload dist/*
fi

echo "Done!"
