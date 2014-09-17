# Inserting Travel time matrix

After doing the normal python dev stuff (setup virtualenv, install
requirements, etc), download [this
file](https://s3.amazonaws.com/travel-time/skims.zip), unpack it into the
``data/raw_data`` folder and run the ``read_transit_skims.py`` file in the main
directory. You’ll need to create a PostgreSQL database and put connection string
into the appropriate place in ``api/app_config.py``.

# Importing Travel Zone data

``shp2pgsql -I -s 3435:4326 Zone09_CMAP_2009.shp | psql``
