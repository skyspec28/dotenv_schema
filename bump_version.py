#!/usr/bin/env python3
"""
Simple script to bump the version in pyproject.toml
Usage: python bump_version.py [major|minor|patch]
"""

import re
import sys
from pathlib import Path

def bump_version(version_type):
    """Bump the version in pyproject.toml"""
    if version_type not in ['major', 'minor', 'patch']:
        print(f"Invalid version type: {version_type}")
        print("Usage: python bump_version.py [major|minor|patch]")
        sys.exit(1)
    
    pyproject_path = Path('pyproject.toml')
    content = pyproject_path.read_text()
    
    # Find the current version
    version_match = re.search(r'version\s*=\s*"(\d+)\.(\d+)\.(\d+)"', content)
    if not version_match:
        print("Could not find version in pyproject.toml")
        sys.exit(1)
    
    major, minor, patch = map(int, version_match.groups())
    
    # Bump the version
    if version_type == 'major':
        major += 1
        minor = 0
        patch = 0
    elif version_type == 'minor':
        minor += 1
        patch = 0
    elif version_type == 'patch':
        patch += 1
    
    new_version = f"{major}.{minor}.{patch}"
    
    # Replace the version in the file
    new_content = re.sub(
        r'version\s*=\s*"\d+\.\d+\.\d+"',
        f'version = "{new_version}"',
        content
    )
    
    pyproject_path.write_text(new_content)
    print(f"Version bumped to {new_version}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bump_version.py [major|minor|patch]")
        sys.exit(1)
    
    bump_version(sys.argv[1])
