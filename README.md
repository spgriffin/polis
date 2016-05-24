# POLIS Footprint Metrics

A CLI tool for computing this metric, see "A Metric for Polygon
    Comparison and Building Extraction Evaluation" by J. Avbelj, et
    al. for more information on the metric.
	
## Installation

You need to have gdal, geos, and libspatialindex installed to use this package.  These are all available in the linux package managers and in brew for OSX, so figure that out first.

Clone this repo, and then navigate to its root.  To install the CLI tool, run
```
pip install .
```
You should now have `polis` available on the command line.

To check out the tool, from the repo's root directory, run
```
polis data/FullSubset.shp data/user_data.shp scores.shp
```
You should see this after a few seconds (in addition to scores.shp being created; it contains the geometies and their score):
```
$ polis data/FullSubset.shp data/user_data.shp data/out.shp
Number of matches: 9
Number of misses: 98608
Duplicate matches: 0
```
