


## Configuring your development environment

- clone this git to you working directory
- install the Plugin Reloader plugin from the QGIS pugin manager
- install QGIS plugin development command line utility pb_tool: `python3 -m pip install pb_tool`
- install nosetests command line tool: `apt-get install python3 nose`
- run test: `make test`
- package the plugin for installation: `pb_tool zip`
- install the zip from `zip_build/hotosm_utils.zip` using the plugin manager
- You can use the Makefile to compile your Ui and resource files when you make changes. This requires GNU make (gmake)


On linux the QGIS plugin directory is located at:
    ~/.local/share/QGIS/QGIS3/profiles/default/python/plugins




For more information, see the PyQGIS Developer Cookbook at:
http://www.qgis.org/pyqgis-cookbook/index.html
