import fiona

# Register format drivers with a context manager

with fiona.drivers():

    # Open a file for reading. We'll call this the "source."

    with fiona.open('gdata/world_borders.shp') as source:

        # The file we'll write to, the "sink", must be initialized
        # with a coordinate system, a format driver name, and
        # a record schema.  We can get initial values from the open
        # collection's ``meta`` property and then modify them as
        # desired.

        meta = source.meta
        meta['schema']['geometry'] = 'Point'

        # Open an output file, using the same format driver and
        # coordinate reference system as the source. The ``meta``
        # mapping fills in the keyword parameters of fiona.open().

        with fiona.open('xx_fiona_1.shp', 'w', **meta) as sink:

            # Process only the records intersecting a box.
            for f in source.filter(bbox=(-107.0, 37.0, -105.0, 39.0)):

                # Get a point on the boundary of the record's
                # geometry.

                f['geometry'] = {
                    'type': 'Point',
                    'coordinates': f['geometry']['coordinates'][0][0]}

                # Write the record out.

                sink.write(f)
