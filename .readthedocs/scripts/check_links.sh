# Check links within a RTD build.

set -e

# Install yq to parse yaml
export YQ_EXE=$(pwd)/yq
wget -q https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -O "$YQ_EXE"
chmod +x "$YQ_EXE"
echo "Installed yq version: $($YQ_EXE --version)"

# Find RTD configuration
readthedocs_config=$(find . \( -name ".readthedocs.yaml" -o -name ".readthedocs.yml" \))
echo "Found RTD config file: $readthedocs_config"

mkdocs_config=$("$YQ_EXE" '.mkdocs.configuration' "$readthedocs_config")
echo "Found MkDocs config: $mkdocs_config"

# Find Python requirements.txt file
python_requirements=$("$YQ_EXE" '.python.install[].requirements' "$readthedocs_config")
echo "Found Python requirements.txt file: $python_requirements"

# Find lychee link-checker config file in `.github/workflows/lychee_config.toml`. 
# If it doesn't exist, use ACCESS-Hive-Docs's one.
lychee_config=.github/workflows/lychee_config.toml
if [ ! -f $lychee_config_path ]; then
    wget -q https://raw.githubusercontent.com/ACCESS-NRI/ACCESS-Hive-Docs/refs/heads/main/${lychee_config_path} -O $lychee_config_path
    echo "Lychee config file not found. Using ACCESS-Hive-Docs' one."
else
    echo "Found Lychee config file."
fi
echo "============= LYCHEE CONFIG ============="
cat $lychee_config
echo "========================================="

# Get repo name from git clone URL
repo=$(sed -E 's|.*github\.com[:/](.+)$|\1|' <<< "$READTHEDOCS_GIT_CLONE_URL")
# Remove .git suffix if present
repo=${repo%.git}
echo "Repo: $repo"
echo "Ref: $READTHEDOCS_GIT_COMMIT_HASH"

# Trigger check_links_workflow with the right inputs
export GITHUB_TOKEN="$GH_WORKFLOW_DISPATCH_TOKEN"
# gh workflow run check_links_workflow.yml --repo ACCESS-NRI/ACCESS-Hive-Docs --ref davide/test_rts -f input1=value1
cat << EOF
gh workflow run check_links_workflow.yml
--repo ACCESS-NRI/ACCESS-Hive-Docs
--ref davide/test_rts
-f repo=${repo}
-f ref=${READTHEDOCS_GIT_COMMIT_HASH}
-f mkdocs_yaml=${mkdocs_config}
-f lychee_config=${lychee_config}
-f lychee_config=${python_requirements}
EOF