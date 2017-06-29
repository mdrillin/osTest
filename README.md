# Superset on OpenShift example

## Summary

The purpose of this demo is to show deployment of Airbnb's Superset to OpenShift.  Initially, the demo includes the Superset deployment plus a Postgresql database with sample data.  The steps to deploy are below.  This process will continue to be refined.

## Deploy the Superset demo to OpenShift
##### Prerequisites
- Access to an OpenShift instance and credentials for login.
- OpenShift command line tools installed to your system
- This git repository cloned to your system

##### Install the demo to OpenShift
The demo can be installed via the script provided in the git repository location on your system.
- cd into the git repo directory.
- edit config.sh to use your OpenShift username and password
- __$ ./setup.sh -h &lt;HOST&gt;__ , where &lt;HOST&gt; is the hostname of your OpenShift instance,
for example __$ ./setups.sh -h http://10.1.2.2:8443__
- please wait for the script to complete - it takes several minutes for the sample data to load.

##### Monitor the deployment in the OpenShift console (eg __https://10.1.2.2:8443/console__ or equivalent)
- Overview will show the deployment in progress.  Can view logs, etc.
- The first deployment will take awhile - as the Dockerfile is processed.

##### Log into the superset console to verify it is active
Once both pods are active, access Superset via the "Route Link".  It may take several minutes before the link is active (while Superset initializes)
- Superset credentials (user: admin, password: superset)

## Create Views / Dashboards in Superset console
log into the Superset console via Route Link (credentials : admin/superset)

##### postgres demo database
The setup script configures the postgres demo database and tables in superset.  You can view available databases using __Sources > Databases__  and available tables using __Sources > Tables__

Available table names in the sample data:
- ROUTE
- DRIVER
- WEATHER_DATA
- TRAFFIC_VIOLATION
- DRIVER_OFFENSE
- CAR_DATA

##### Superset 'slices'
The setup script also configures 'slices'.  You can view the slices by clicking on the __Slices__ tab.

If you want to create new slices, you can do that as follows:

- Sources > Tables
- Click on a table name --> takes you to explorer view

- Choose Visualization Type, eg TableView
- in GROUP BY section, remove "Count(*)" under metrics

- in NOT GROUPED BY section, click columns and add...

- Click "Query" to test the slice.  When finished, click "Save" to save the slice with a name

##### Superset Dashboards
The setup script configures a demo dashboard.  You can view the dashboard by clicking on the __Dashboards__ tab.

If you want to create a new dashboard, you can do that as follows:

- Add a new dashboard and name it.
- You can then add any of the available slices to the dashboard.



