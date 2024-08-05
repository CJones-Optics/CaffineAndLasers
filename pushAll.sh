#!/bin/bash

# Simple Bash Script to add, commit and push all changes to a git repository
# Usage: ./gitpush.sh "Commit Message"

git add .
git commit -m "$1"
git push

echo "Changes pushed to repository"
