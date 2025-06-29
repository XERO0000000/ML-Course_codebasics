#!/bin/bash

# === CONFIGURATION ===
REPO_URL="https://github.com/XERO0000000/ML-Course_codebasics.git"
BRANCH="main"
COMMIT_MESSAGE="${1:-Auto update}"  # You can pass a custom commit message

# === SCRIPT START ===
echo "📁 Syncing current folder to GitHub..."

# Initialize git repo if not already
if [ ! -d ".git" ]; then
    echo "🔧 Initializing Git repository..."
    git init
fi

# Add remote if not already added
if ! git remote | grep -q "origin"; then
    echo "🔗 Adding remote origin..."
    git remote add origin "$REPO_URL"
fi

# Add files and commit
echo "➕ Adding files..."
git add .

echo "📝 Committing changes..."
git commit -m "$COMMIT_MESSAGE"

# Push to GitHub
echo "🚀 Pushing to GitHub..."
git push -u origin "$BRANCH"

echo "✅ Done!"
