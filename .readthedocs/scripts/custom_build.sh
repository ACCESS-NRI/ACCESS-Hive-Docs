# This is a custom build script for mkdocs that checks for the branch name and exports 
# a EDIT_URI env variable to be used in the mkdocs build to set edit_uri to the proper branch, 
# especially for PR preview builds.
# If the build comes from a forked repo or from a tag, the EDIT_URI variable will not be set.
# This is needed to avoid the link-check workflow to fail for new pages if the edit_uri points to 
# a non-existing file in the main branch.

set -e

if [ "$READTHEDOCS_VERSION_TYPE" == external ]; then # PR preview build
    # Download jq
    export JQ_EXE=$(pwd)/jq
    wget -q https://github.com/stedolan/jq/releases/latest/download/jq-linux64 -O "$JQ_EXE"
    chmod +x "$JQ_EXE"
    "$JQ_EXE" --version
    # Get full repo
    full_repo=$(sed -E 's|.*github\.com[:/](.+)$|\1|' <<< "$READTHEDOCS_GIT_CLONE_URL")
    # Remove .git suffix if present
    full_repo=${full_repo%.git}
    # Get repo and owner
    IFS='/' read owner repo <<< "$full_repo"
    # Check if the PR comes from a forked repo
    gh_api_url="https://api.github.com/repos/$owner/$repo"
    pr_info=$(curl -s "$gh_api_url/pulls/$READTHEDOCS_GIT_IDENTIFIER")
    pr_head_owner=$("$JQ_EXE" -r '.head.user.login' <<< "$pr_info")
    if [ "$owner" == "$pr_head_owner" ]; then # Not a fork
        # Get the branch name
        branch_name=$("$JQ_EXE" -r '.head.ref' <<< "$pr_info")
    fi
elif git show-ref --heads "$READTHEDOCS_GIT_IDENTIFIER" --quiet; then # Branch build
    branch_name="$READTHEDOCS_GIT_IDENTIFIER"
fi

# Download yq
export YQ_EXE=$(pwd)/yq
wget -q https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -O "$YQ_EXE"
chmod +x "$YQ_EXE"
"$YQ_EXE" --version

# Get RTD config path
rtd_config_path=$(find "$READTHEDOCS_REPOSITORY_PATH" -type f \( -name ".readthedocs.yaml" -o -name ".readthedocs.yml" \))
# Get mkdocs config path
mkdocs_path=$("$YQ_EXE" '.mkdocs.configuration' "$rtd_config_path")
if [ -n "$branch_name" ]; then
    # Get docs_dir from mkdocs config or set to default 'docs'
    docs_dir=$("$YQ_EXE" '.docs_dir // "docs"' "$mkdocs_path")
    EDIT_URI="edit/$branch_name/$docs_dir"
    echo "This is a branch build. EDIT_URI set to to '$EDIT_URI'"
    export EDIT_URI
fi

# Default RTD mkdocs build commands
echo ======= START OF mkdocs.yml =======
cat "$mkdocs_path"
echo ======= ENF OF mkdocs.yml =======
cmd="python -m mkdocs build --clean --site-dir $READTHEDOCS_OUTPUT/html --config-file $mkdocs_path"
eval "$cmd"