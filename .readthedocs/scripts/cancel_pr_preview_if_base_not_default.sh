# Cancel PR previews when the PR base is not the default branch
# To cancel a build, exit with the return code 183 
# https://docs.readthedocs.com/platform/stable/build-customization.html#cancel-build-based-on-a-condition
set -e

# Don't run this job if the build is not for a PR preview (i.e., version type is not "external")
[ "$READTHEDOCS_VERSION_TYPE" != external ] && exit 0
        
# Install jq to parse JSON
JQ_EXE=$(pwd)/jq
curl -L -o $JQ_EXE https://github.com/jqlang/jq/releases/download/jq-1.8.1/jq-linux64
chmod +x $JQ_EXE
echo "Installed jq version: $($JQ_EXE --version)"

# Get repo name from git clone URL
REPO=$(sed -E 's|.*github\.com[:/](.+)$|\1|' <<< "$READTHEDOCS_GIT_CLONE_URL")
# Remove .git suffix if present
REPO=${REPO%.git}
echo "Repo: $REPO"

# Get PR base
PR_BASE=$(curl -s "https://api.github.com/repos/${REPO}/pulls/${READTHEDOCS_GIT_IDENTIFIER}" | $JQ_EXE -r '.base.ref')
echo "PR base: $PR_BASE"

# Get default branch
DEFAULT_BRANCH=$(curl -s "https://api.github.com/repos/${REPO}" | $JQ_EXE -r ".default_branch")
echo "Default branch: $DEFAULT_BRANCH"

if [[ "$PR_BASE" == "$DEFAULT_BRANCH" ]]; then
    echo "PR base is the default branch, continuing with the PR preview build..."
    exit 0
else
    echo "PR base is not the default branch, build cancelled."
    exit 183
fi