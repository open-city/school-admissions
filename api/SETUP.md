# Download and load database

A dump of the database can be downloaded [here](http://travel-time.s3.amazonaws.com/schools_db.sql.gz).

To load it, do something like this:

```
$ createdb schools_db
$ wget http://travel-time.s3.amazonaws.com/schools_db.sql.gz
$ gunzip schools_db.sql.gz
$ psql -f schools_db.sql
```


# Build the database on your own

If you like, you can also build the database on your own. The components are:

* [Transit skims](https://travel-time.s3.amazonaws.com/skims.zip)
* [2014-2015 School locations](https://data.cityofchicago.org/api/geospatial/3fhj-xtn5?method=export&format=Shapefile)
* [Zone Shapefile](http://travel-time.s3.amazonaws.com/Zone09_CMAP_2009.zip)

### Load school locations and zones

Both the school locations shapefile and the CMAP zones shapefile use the
[Illinois State Plane spatial reference
system](http://spatialreference.org/ref/epsg/3435/). To make sure these play
nicely with a web map, we’ll reproject the coordinates as we import them into
the database using the
[``shp2pgsql``](http://postgis.net/docs/manual-2.0/using_postgis_dbmanagement.html#shp2pgsql_usage)
tool that ships with PostGIS.

```
$ shp2pgsql -I -s 3435:4326 Zone09_CMAP_2009.shp | psql -d schools
$ shp2pgsql -I -s 3435:4326 CPS_School_Locations_SY1415.shp | psql -d schools
```

### Load transit skims

The three files we are interested in to begin with are the ones that give the
"in vehicle time", "wait time" and "walk / transfer time" for a given trip
between two zones. Each of these legs is contained within a different file.
Each of the folders with numeric names contain the transit time projections for
different years. The files we are using for this project are in the ``100_2010``
folder. The three files are ``mf22.txt``, ``mf23.txt`` and ``mf24.txt``.

