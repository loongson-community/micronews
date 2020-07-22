#!/bin/bash

set -e

echo "REPO: $GITHUB_REPOSITORY"
echo "ACTOR: $GITHUB_ACTOR"
echo "ISSUE: $GITHUB_ISSUE"

echo '=================== Install Requirements ==================='
pip install -r requirements.txt
echo '=================== Setup environment ==================='
remote_repo="https://x-access-token:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"
git remote add gh_push "$remote_repo"
git config user.name "${GITHUB_ACTOR}"
git config user.email "${GITHUB_ACTOR}@users.noreply.github.com"
echo '=================== Make Post ==================='
./add.py -i "${GITHUB_ISSUE}" -y
echo '=================== Push to GitHub ==================='
git push gh_push
echo '=================== Done  ==================='