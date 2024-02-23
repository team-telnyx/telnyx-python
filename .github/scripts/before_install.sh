#!/bin/bash

# Install the necessary tools
npm install -g @stoplight/prism-cli

# Variable for original and modified OpenAPI spec files
original_spec="/tmp/original_spec.json"
modified_spec="/tmp/modified_spec.json"

# Download the OpenAPI spec file
curl "${TELNYX_MOCK_OPEN_API_URI}" -o "${original_spec}"

# Use a tool like jq to modify the file (you may need to install jq or another JSON processor)
jq '.paths |= with_entries(.key |= "/v2" + .)' "${original_spec}" > "${modified_spec}"

echo "Starting up Prism Mock Server with modified spec file"
prism mock "${modified_spec}" > /dev/null &

# Your existing setup for the Telnyx Prism Mock (if needed)
git clone https://github.com/team-telnyx/telnyx-prism-mock.git
cd telnyx-prism-mock/proxy
npm install
node index.js > /dev/null &
cd -