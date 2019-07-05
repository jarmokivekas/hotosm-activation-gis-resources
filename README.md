# HOTOSM Activation GIS workflows

This file is a compilation of notes made during the Peru Activation regarding procedures and toolchains that work well.

Most practical in this reporsitory are based to QGIS version 3.4 or 3.6, but any up-to-date version should do.


# TM Projects With Multiplt Villages

In areas where there are a large amount of small dispersed villages, it's effective to create individual tasks for the villages in the project.

We user project [#6061 – Peru remote villages](https://tasks.hotosm.org/project/6061#bottom) as an example.

![](img/6061-remote-village-screenshot.png)

##  Estimate the locations of villages.

Build a layer with at least one feature per village.

In #6061 was created using a point layer consisting of:

- OSM nodes tagged as "place"="village" or "place"="hamlet"
- OSM nodes tagged as "amenity"="school"
- Peru national data record hosted by GeoIDEP helped finding settlements ("Lugares Poblados") with > 150 population


Choosing which tags to target is a manual process. In #6061 it was lucky that the location information of shools in Peru had already been imported to OSM. Many villages had no other mapping done (no buildings, roads etc.) except for one "amenity"="school" node.

Manually adding points may be necessary in some cases.

## Building the Tasking Manager Project.

Create a buffer around the estimated locations of the villages to create task boundaries. #6061 used a 500m buffer around point coordinates. The majority of small villages were able to fit inside the 500m buffer, but larger villages will extend beyond. Keep in mind that if the buffer is too large adjacent villages may end merging into one task that includes both villages. With a 500m buffer some villages still merged, but it was not an issue, mappers simply mapped both villages.

The _Interest features to TM project tasks_ does this process automatically. Set the output to a `.geojson` file, and it will be directly compatible with TM.
![interest-features-to-tm-project-tasks.png](img/interest-features-to-tm-project-tasks.png)

Same process manually:

1. *Reproject* POIs to something suitable, such as *EPSG:3857* (WGS 84 Pseudo Mercator), where the coordinate unit is meters instead of degrees. Vector > Data Management Tools > Reproject Layer
3. *Buffer* points of interest by 500m. Vector > Geoprocessing Tools > Buffer
4. *Dissolve* buffered areas so that overlapping areas are combined into one polygon. Vector > Geoprocessing Tools > Dissolve
5. In the dissolve output, split any possible *mulitpart polygons to singleparts*. Vector > Geometry Tools > Multipart to Singleparts
6. Export features to *Geojson*, making sure to use the CRS *EPSG:4326* (WGS84). Right-click layer > Export > Save Features As
7. Use the exported file as the task geometry in Tasking Manager.

## Notes on #6061 - Peru remote villages

1. Mappers should be explicitly instructed to map _outside_ the task area when needed since task are not adjacent. Some mappers will obey task the boundary, leaving the areas outside unmapped. Especially make sure validators are aware as well.
2. Project #6061 consisted of 379 tasks spread along two larger rivers. For quick results, the project should have been split into at least two smaller projects, one per river. That way it would have been faster to produce contiguous areas of validated data. For large TM projects it takes a long time to have the entire area mapped and validated so that reliable maps can be created.

# GIS workflows

## Estimating the need for further mapping

Project #6061 had a total of 379 tasks, each corresponding to individual villages, ideally. *Question*: How many have a landuse=residential polygon mapped?

1. Obtain and import the task geometry from Tasking Manager as a geojson file, availlable directly from the api. http://tasks.hotosm.org/api/v1/project/6061/tasks.
2. Obtain and import the existing landuse=residential polygons from the OSM database (overpass api, HOT Export Tool, JSOM, QuickOSM)
3. Reduce the landuse polygons to vertices. Vector > Geometry Tools > Extract Vertices.
4. Count how many landuse polygon vertices are inside each of the TM task areas, and add the information to the task polygon. If there is not landuse polygon, the vertex count will be 0. Vector > Analysis Tools > Count Points in Polygon
5. Filter the task areas of the  resulting layer based on the vertex count. Right-click layer > Filter. Use a filter such as `"NUMPOINTS" = 0` to show only task areas with missing.

This method is applicable to any mapping features, e.g. roads, buildings.


## Obtaining OSM data

The HOT Export tool is good for this, especially for large areas. The QGIS QuickOSM plugin is convenient for downloading OSM data directly into QGIS using overpass turbo.

# Creating Exports of a TM Project

## Choosing the export area

When exporting data for one city / population center:

1. The area should include the Tasking Manager project area
2. Consider exporting a larger area to include major terrain landmarks. In that case of #6059 - Lagunas, the export included a section of the nearby river. If a map of a riverside city does not show a river, it can be confusing. Consider someone giving practical direction on the ground, "go two blocks toward the river."
3. Consider exporting a larger area to include connecting roads
4. Avoid including areas with missing/unvalidated data.
5. If able, stick to convex shapes for export areas. Missing data in the middle of a map is confusing.

## Choosing what features to export

Exports in the Peru Activation used the HDX preset in the HOT Export Tool. It includes buildings, roads, waterways and POIs (amenities, etc.).

1. The HDX preset is sane for generic basemaps
2. For #6061, remote villages, landuse=residential polygons were added to the HDX preset YAML, as those were mapped during the project.
3. Try to use a consistent YAML config file throughout the activation in different export products when possible.

## Export file formats

- Shapefile, because it has wide support
- Geopackage, modern Shapefile alternative
- Garmin IMG for handheld devices
- Google Earth KML, sure. Google Earth Pro (desktop version) supports ESRI shapefiles, though.


# Useful QGIS plugins

- *QuickMapServices* provides TMS raster tile basemaps, including OSM tiles as well as Bing Aerial and Digital Globe Premium satellite imagery, which is are the primary sources of the OSM data in this activation-
- *Quick OSM* has a useful JOSM Remote feature, which uses the JSOM remote control to set the editing area to match the current QGIS canvas area.
- *Quick OSM* can query overpass turbo with a very simple interface. This is useful for downloading OSM data for validation/analysis for a large area.
- *OSMDownloader* allows downloading data from the OSM database into .osm files from QGIS by simple rectangle selection. QuickOSM is often more convenient

When QuickOSM or OSMDownloader fail to download large datasets, use the HOT Export Tool.

# uMap collection of smaller dataset

uMap is quick and easy to use tool for sharing geodata.

- Give validatos exlicit areas of interest to validate, uMap has built-in josm remote and iD launcher.
- display all Tasking Manager projects for an activation in one map.
- display areas where pre-made exports are available
- display data that can be automatically update on the backend (see below)

## Live interactive maps using uMap + github

1. create a GIS dataset / AOI using e.g QGIs
2. export to geojson using the CRS EPSG:4326 (WGS84)
3. upload the geojson to github.
    - Use Github from the browser, or a git client
    - Minimal set of commands on commandline: `git add datasets; git commit; git push origin master;`
4. supply the GitHub link to the file as the input dataset in uMap.
5. update the uMap whenever by pushing a new version of the file to GitHub


## Reference Layers for JSOM

JOSM has somewhat limited ability to read in GIS datasets. To create gpx files with QGIS that are compatible with JSOM:

1. Convert multiparts to singleparts
2. Convert polygons to lines
3. Reproject to EPSG:4326 WGS84
4. Disable all data fileds in the export to gpx
5. JOSM: File > Open, choose gpx file


# Tasking Manager Hidden Features

These are not quite _features_ but API endpoint that are often useful

## Download Task Squares

Download TM project task squares as a geojson file (project #6060 in this case) directly from the API: https://tasks.hotosm.org/api/v1/project/6060?as_file

The _Download TM Project Geojson File_ QGIS model in this repository uses this API endpoint.
