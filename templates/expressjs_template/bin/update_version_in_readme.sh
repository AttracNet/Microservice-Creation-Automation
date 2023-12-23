#!/bin/bash

# Read version from version.txt
version=$(cat version.txt)

# Check if the version needs updating
if grep -q "^Version: $version$" README.md; then
  echo "Version in README.md is already up-to-date."
else
  # Check the operating system
  if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS sed syntax
    sed -i '' "s/^Version: .*/Version: $version/" README.md
  else
    # Linux sed syntax
    sed -i "s/^Version: .*/Version: $version/" README.md
  fi

  echo "Version updated to $version in README.md"
fi
