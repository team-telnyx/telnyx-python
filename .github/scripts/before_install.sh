#!/bin/bash

# Abort on errors
set -e

# Ensure jq and curl are installed
sudo apt-get update && sudo apt-get install -y jq curl

# Install the necessary tools (specify Node.js version as needed)
npm install -g @stoplight/prism-cli

# Variable for original and modified OpenAPI spec files
original_spec="/tmp/original_spec.json"
modified_spec="/tmp/modified_spec.json"

# Download the OpenAPI spec file
curl "${TELNYX_MOCK_OPEN_API_URI}" -o "${original_spec}"

# Modify the file using jq
jq '.paths |= with_entries(.key |= "/v2" + .)' "${original_spec}" > "${modified_spec}"

echo "Starting up Prism Mock Server with modified spec file"
prism mock "${modified_spec}" > prism.log 2>&1 &

# Your existing setup for the Telnyx Prism Mock (if needed)
git clone https://github.com/team-telnyx/telnyx-prism-mock.git
cd telnyx-prism-mock/proxy
npm install
node index.js > proxy.log 2>&1 &
cd -