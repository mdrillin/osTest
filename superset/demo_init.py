from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
#
# Creates demo database, dashboard, and slices.
#
import os
import json

from sqlalchemy import String, DateTime, Date, Float, BigInteger
from superset import app, db
from superset.models import core as models
from superset.connectors.connector_registry import ConnectorRegistry

Slice = models.Slice
Dash = models.Dashboard
TBL = ConnectorRegistry.sources[ 'table' ]

DEMO_DB_NAME = "demo"
demo_slices = []

#def testoutput():
#    file = open("/superset/pythonoutput.txt", "w")
#    file.write("help me!")
#    file.close()

def getPostgresUri():
    demoDbName = os.environ.get( "DB_DATABASE" )
    demoDbUser = os.environ.get( "DB_USERNAME" )
    demoDbPswd = os.environ.get( "DB_PASSWORD" )
    osAppName = os.environ.get( "APPLICATION_NAME" )
    osProjectName = "superset"
    demoDbUri = "postgresql+psycopg2://" + demoDbUser + ":" + demoDbPswd + "@" + osAppName + "-postgresql." + osProjectName + ".svc.cluster.local:5432/" + demoDbName
    return demoDbUri

def get_or_create_demo_db():
    dbobj = (
        db.session.query( models.Database )
                  .filter_by( database_name = DEMO_DB_NAME )
                  .first()
    )

    if not dbobj:
        dbobj = models.Database(database_name = DEMO_DB_NAME )
        dbobj.set_sqlalchemy_uri( getPostgresUri() )
        dbobj.expose_in_sqllab = True
        dbobj.allow_run_sync = True
        db.session.add( dbobj )
        db.session.commit()

    return dbobj

def merge_slice( slc ):
    o = db.session.query( Slice ).filter_by( slice_name = slc.slice_name ).first()

    if o:
        db.session.delete( o )

    db.session.add( slc )
    db.session.commit()

#
# DRIVER table and slice
#
def create_driver():
    print( "Creating DRIVER table and slice" )

    tbl_name = 'DRIVER'
    tbl = db.session.query( TBL ).filter_by( table_name = tbl_name ).first()
    
    if not tbl:
        tbl = TBL( table_name = tbl_name )
        tbl.description = "A collection of drivers."
        tbl.database = get_or_create_demo_db()
        db.session.merge( tbl )
        db.session.commit()
        tbl.fetch_metadata()

#    slc = Slice(
#        slice_name = "Drivers",
#        viz_type = 'table',
#        datasource_type = 'table',
#        datasource_id = tbl.id,
#    )
#
#    demo_slices.append( slc.slice_name )
#    merge_slice( slc )

#
# CAR_DATA table and slice
#
def create_car_data():
    print( "Creating CAR_DATA table and slice" )

    tbl_name = 'CAR_DATA'
    tbl = db.session.query( TBL ).filter_by( table_name = tbl_name ).first()
    
    if not tbl:
        tbl = TBL( table_name = tbl_name )
        tbl.description = "Car data for each route."
        tbl.database = get_or_create_demo_db()
        db.session.merge( tbl )
        db.session.commit()
        tbl.fetch_metadata()

#    slc = Slice(
#        slice_name = "CarData",
#        viz_type = 'table',
#        datasource_type = 'table',
#        datasource_id = tbl.id,
#    )

#    demo_slices.append( slc.slice_name )
#    merge_slice( slc )

#
# DRIVER_OFFENSE table and slice
#
def create_driver_offenses():
    print( "Creating DRIVER_OFFENSE table and slice" )

    tbl_name = 'DRIVER_OFFENSE'
    tbl = db.session.query( TBL ).filter_by( table_name = tbl_name ).first()
    
    if not tbl:
        tbl = TBL( table_name = tbl_name )
        tbl.description = "A collection of driver traffic violations."
        tbl.database = get_or_create_demo_db()
        db.session.merge( tbl )
        db.session.commit()
        tbl.fetch_metadata()

#    slc = Slice(
#        slice_name = "DriverOffenses",
#        viz_type = 'table',
#        datasource_type = 'table',
#        datasource_id = tbl.id,
#    )
#
#    demo_slices.append( slc.slice_name )
#    merge_slice( slc )

#
# ROUTE table and slice
#
def create_route():
    print( "Creating ROUTE table and slice" )

    tbl_name = 'ROUTE'
    tbl = db.session.query( TBL ).filter_by( table_name = tbl_name ).first()
    
    if not tbl:
        tbl = TBL( table_name = tbl_name )
        tbl.description = "A collection of routes."
        tbl.database = get_or_create_demo_db()
        db.session.merge( tbl )
        db.session.commit()
        tbl.fetch_metadata()

#    slc = Slice(
#        slice_name = "Routes",
#        viz_type = 'table',
#        datasource_type = 'table',
#        datasource_id = tbl.id,
#    )
#
#    demo_slices.append( slc.slice_name )
#    merge_slice( slc )

#
# TRAFFIC_VIOLATION table and slice
#
def create_traffic_violation():
    print( "Creating TRAFFIC_VIOLATION table and slice" )

    tbl_name = 'TRAFFIC_VIOLATION'
    tbl = db.session.query( TBL ).filter_by( table_name = tbl_name ).first()
    
    if not tbl:
        tbl = TBL( table_name = tbl_name )
        tbl.description = "The collection of known traffic violations."
        tbl.database = get_or_create_demo_db()
        db.session.merge( tbl )
        db.session.commit()
        tbl.fetch_metadata()

#    slc = Slice(
#        slice_name = "TrafficViolations",
#        viz_type = 'table',
#        datasource_type = 'table',
#        datasource_id = tbl.id,
#    )
#
#    demo_slices.append( slc.slice_name )
#    merge_slice( slc )

#
# WEATHER_DATA table and slice
#
def create_weather_data():
    print( "Creating WEATHER_DATA table and slice" )

    tbl_name = 'WEATHER_DATA'
    tbl = db.session.query( TBL ).filter_by( table_name = tbl_name ).first()
    
    if not tbl:
        tbl = TBL( table_name = tbl_name )
        tbl.description = "Weather data for each route."
        tbl.database = get_or_create_demo_db()
        db.session.merge( tbl )
        db.session.commit()
        tbl.fetch_metadata()

#    slc = Slice(
#        slice_name = "WeatherData",
#        viz_type = 'table',
#        datasource_type = 'table',
#        datasource_id = tbl.id,
#    )
#
#    demo_slices.append( slc.slice_name )
#    merge_slice( slc )


