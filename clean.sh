#!/bin/bash

#################
#
# Show help and exit
#
#################
function show_help {
	echo "Usage: $0 -h"
	echo "-d - delete the project"
	echo "-h - ip|hostname of Openshift host"
  exit 1
}

if [ ! -f config.sh ]; then
    echo "No config file found .. exiting"
    exit 1
fi

#
# Source the configuration
#
. ./config.sh

#
# Determine the command line options
#
while getopts "h:d" opt;
do
	case $opt in
	d) KILL_PROJECT=1 ;;
	h) OS_HOST=$OPTARG ;;
	*) show_help ;;
	esac
done

if [ -z "$OS_HOST" ]; then
  echo "No Openshift host specified. Use -h <host|ip>"
  exit 1
fi

echo -e '\n\n=== Logging into oc tool as admin user ==='
oc login ${OS_HOST} -u ${OPENSHIFT_USER} -p ${OPENSHIFT_PASSWD}
oc whoami 2>&1 > /dev/null || { echo "Cannot log in ... exiting" && exit 1; }

echo -e '\n\n=== Deleting openshift resources'

# Change to project
oc project ${OPENSHIFT_PROJECT}

# Delete application resources
oc delete all -l app=${OPENSHIFT_APPLICATION_NAME}  || { echo "WARNING: Could not delete old application resources" ; }

# Delete the project
if [ -n "${KILL_PROJECT}" ]; then
  oc delete project ${OPENSHIFT_PROJECT}
else
  echo "\n== Project not deleted: -d arg not supplied =="
fi

echo `oc whoami` "still logged in; use 'oc logout' to logout of openshift"

echo -e "\n\n==============================================="
echo "Done with cleanup"
echo "==============================================="

