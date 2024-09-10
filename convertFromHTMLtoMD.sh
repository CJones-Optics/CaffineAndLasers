#!/bin/bash

# Simple script which searches for all .html fles in blogsHTML
# and converts them to .md files in blogsMD

# Check if blogsMD exists, if not create it
if [ ! -d "blogsMD" ]; then
  mkdir blogsMD
fi

# Loop through all .html files in blogsHTML
for file in ./blogsHTML/*.html
do
  # Get the filename without the extension
  filename=$(basename "$file" .html)
  echo "Converting $filename.html to $filename.md"
  # Convert the file to .md
  pandoc -s "$file" -o "blogsMD/$filename.md"
done
