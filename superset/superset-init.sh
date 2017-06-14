#!/bin/bash

set -eo pipefail

# set up Superset if we haven't already
if [ ! -f ./.setup-complete ]; then
  echo "Running first time setup for Superset"

  echo "Creating admin user ${ADMIN_USERNAME}"
  cat > ./admin.config <<EOF
${ADMIN_USERNAME}
${ADMIN_FIRST_NAME}
${ADMIN_LAST_NAME}
${ADMIN_EMAIL}
${ADMIN_PWD}
${ADMIN_PWD}

EOF

  /bin/sh -c '/usr/local/bin/fabmanager create-admin --app superset < ./admin.config'

  rm ./admin.config

fi
