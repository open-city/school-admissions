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

(details coming...)

### Load transit skims

(details coming...)
