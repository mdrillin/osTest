#!/bin/bash

###
#
# Installs and configures the superset demo on OpenShift
#
###

#################
#
# Show help and exit
#
#################
function show_help {
	echo "Usage: $0 -h"
	echo "-h - ip|hostname of Openshift host"
  exit 1
}

if [ ! -f 'config.sh' ]; then
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
while getopts "h:" opt;
do
	case $opt in
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

echo -e '\n\n=== Creating a new project ==='
oc new-project ${OPENSHIFT_PROJECT}
echo "Switch to the new project, creating it if necessary"
{ oc get project ${OPENSHIFT_PROJECT} 2>&1 >/dev/null && \
	oc project ${OPENSHIFT_PROJECT}; } || \
	oc new-project ${OPENSHIFT_PROJECT} || \
	{ echo "FAILED: Could not use indicated project ${OPENSHIFT_PROJECT}" && exit 1; }

echo -e '\n\n=== Deploying superset demo from template with config values ==='
oc get dc/${OPENSHIFT_APPLICATION_NAME} 2>&1 >/dev/null || \
	oc new-app superset-template.json \
		--name=${OPENSHIFT_APPLICATION_NAME} \
		--param=APPLICATION_NAME=${OPENSHIFT_APPLICATION_NAME} \
		--param=DB_DATABASE=${POSTGRES_DATABASE} \
		--param=DB_USERNAME=${POSTGRES_USERNAME} \
		--param=DB_PASSWORD=${POSTGRES_PASSWORD} \
		-l app=${OPENSHIFT_APPLICATION_NAME}

echo -e '\n\n=== Waiting 30 sec for postgres pod to deploy, before attempting to load data ==='
sleep 30s

fullpgpod=$(oc get pod -o name --selector="deploymentConfig=${OPENSHIFT_APPLICATION_NAME}-postgresql")
pgpod=$(echo $fullpgpod | cut -d '/' -f 2)
echo -e '\n\n=== Loading data into postgres db pod ['$pgpod'] -- This takes several minutes - Please Wait! ==='
 
oc exec -i ${pgpod} -- /bin/sh -i -c "psql -h 127.0.0.1 -U ${POSTGRES_USERNAME} -q -d ${POSTGRES_DATABASE}" < initial_data.sql

echo "==============================================="
echo "Done"
echo "==============================================="

