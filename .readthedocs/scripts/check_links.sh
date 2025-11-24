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
default_lychee_config_path='.github/workflows/lychee_config.toml'
if [ ! -f "$default_lychee_config_path" ]; then
    echo "Lychee config file not found. Using ACCESS-Hive-Docs' one."
    lychee_config=
else
    echo "Found Lychee config file."
    lychee_config="$default_lychee_config_path"
fi

# Get repo name from git clone URL
repo=$(sed -E 's|.*github\.com[:/](.+)$|\1|' <<< "$READTHEDOCS_GIT_CLONE_URL")
# Remove .git suffix if present
repo=${repo%.git}
echo "Repo: $repo"
# Get git ref. If it's a PR (i.e., version type is "external"), 
# we use the PR number (this also handles cases when the PR is 
# from a fork), otherwise we use the commit hash.
if [ "$READTHEDOCS_VERSION_TYPE" == external ]; then
    ref="refs/pull/${READTHEDOCS_GIT_IDENTIFIER}/head"
else
    ref="$READTHEDOCS_GIT_COMMIT_HASH"
fi
echo "Ref: $ref"

# Trigger check_links workflow with the right inputs
cat << EOF
curl -L 
  -X POST 
  -H "Accept: application/vnd.github+json" 
  -H "Authorization: Bearer $GH_WORKFLOW_DISPATCH_TOKEN" 
  https://api.github.com/repos/${repo}/actions/workflows/check_links.yml/dispatches 
  -d "{
    \"ref\": \"davide/test_rtd\",
    \"inputs\": {
      \"ref\": \"${ref}\",
      \"mkdocs_yaml\": \"${mkdocs_config}\",
      \"lychee_config\": \"${lychee_config}\",
      \"python_requirements_txt\": \"${python_requirements}\",
      \"base_url\": \"${READTHEDOCS_CANONICAL_URL}\"
    }
  }"
EOF

curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $GH_WORKFLOW_DISPATCH_TOKEN" \
  https://api.github.com/repos/${repo}/actions/workflows/check_links.yml/dispatches \
  -d "{
    \"ref\": \"davide/test_rtd\",
    \"inputs\": {
      \"ref\": \"${ref}\",
      \"mkdocs_yaml\": \"${mkdocs_config}\",
      \"lychee_config\": \"${lychee_config}\",
      \"python_requirements_txt\": \"${python_requirements}\",
      \"base_url\": \"${READTHEDOCS_CANONICAL_URL}\"
    }
  }"