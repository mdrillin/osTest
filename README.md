# Superset on Openshift example

## Summary

Purpose is to demostrate deployment of Airbnb's superset to OpenShift.  Initially, the demo includes the superset deployment plus a Postgresql database with sample data.  The steps to deploy are below.  This process will continue to be refined.

## Deploy the OpenShift demo app
##### Create a new project
$ oc new-project test

##### Deploy the app
$ oc new-app -f https://raw.githubusercontent.com/mdrillin/osTest/master/superset-template.json

##### Monitor the deployment in the OpenShift console (eg https://10.1.2.2:8443/console or equivalent)
- Overview will show the deployment in progress.  Can view logs, etc.
- The first deployment will take awhile - as dockerfile is processed.

##### Log into the superset console to verify it is active
Once both pods are active, access superset via the "Route Link"
- superset credentials (user: admin, password: superset)

## Load Postgres sample data

##### Get a local copy of the data (initial_data.sql)
https://raw.githubusercontent.com/mdrillin/osTest/master/initial_data.sql

##### get the postgres pod name
$ oc get pods

##### use the pod name to load postgres data from initital_data.sql, for example
$ oc exec -i superset-demo-postgresql-1-ru0zb -- /bin/sh -i -c 'psql -h 127.0.0.1 -U pguser -q -d pgdb' < initial_data.sql
- Wait for loading to complete - there is no logging and it takes a few minutes!

## Create Views / Dashboards in superset console
log into the superset console via Route Link (credentials : admin/superset)

##### Add the postgres database

Sources > Databases,  click "+" to add new database
- Database name   : postgresql
- SQL Alchemy URI : postgresql+psycopg2://pguser:pguser@superset-demo-postgresql.[projectName].svc.cluster.local:5432/pgdb

example for project 'test'
- postgresql+psycopg2://pguser:pguser@superset-demo-postgresql.test.svc.cluster.local:5432/pgdb

- Click 'Test Connection' to verify connection
- Click Save

##### Add the postgres database tables
- Sources > Tables, click "+" to add new table
- Choose Database = postgresq
- Enter the table name, then click Save

Available table names in the sample data:
- ROUTE
- DRIVER
- WEATHER_DATA
- TRAFFIC_VIOLATION
- DRIVER_OFFENSE
- CAR_DATA

##### Create a 'slice' to view the data
- Sources > Tables
- Click on a table name --> takes you to explorer view

- Choose Visualization Type, eg TableView
- in GROUP BY section, remove "Count(*)" under metrics

- in NOT GROUPED BY section, click columns and add...

- Click "Query" to test the slice.  When finished, click "Save" to save the slice with a name

##### Create Dashboards
- Add a new dashboard and name it.
- Can add any of the slices created previously to the dashboard.



