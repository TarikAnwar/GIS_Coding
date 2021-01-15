"""
Function used to facilitate the workflow of a remote sensing, satellite image machine learning project.
The task was to create shapefiles for corresponding amount of satellite images that were to be digitized in arcmap.
This code helped to speed up the process of matching specified amount of .shp files for corresponding .tif files
instead of always manually creating them one by one.
"""

import arcpy


def create_shapefile(number,output_directory):
    for i in range(number):
        output_directory="file_path"
        arcpy.CreateFeatureclass_management(output_directory,"file_name"+str(i)+".shp","POLYGON")



