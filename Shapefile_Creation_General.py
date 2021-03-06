"""
A function that can be used when wanting to quickly generate set amount of empty shapefiles with no specific attributes from templates. 
The function takes in an integer argument, as well as the output path. 

"""

import arcpy


def create_shapefile(number,output_directory):
    for i in range(number):
        output_directory="file_path"
        arcpy.CreateFeatureclass_management(output_directory,"file_name"+str(i)+".shp","POLYGON")