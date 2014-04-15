GIS utility to join csv tables to shapefiles

**Dependencies**
- [Fiona](https://pypi.python.org/pypi/Fiona)
- [GDAL/OGR](http://www.gdal.org/ogr/)
- [Pandas](http://pandas.pydata.org) and [NumPy](http://www.numpy.org)

###Use

**Usage:** `python fiona_join.py <in.shp> <shpkey> <in.csv> <csvkey> <out.shp>`

Performs a [left join](http://en.wikipedia.org/wiki/Join_(SQL)#Left_outer_join) of the csv to the shapefile on the given keys. Saves result in `<out.shp>`.

###Tests

`tests.py`

