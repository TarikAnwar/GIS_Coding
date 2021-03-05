"""

Script used to generate empty shapefiles for a machine learning feature detection project.
Project involved creation of empty shapefiles in ArcMap for building digitization of specific satellite image chips 
in order to train the alorithm. 
Each polygon shapefile had to have the same name as the corresponding .tif files in directory.
The script first generates the empty shapefiles from a template with specific attributes,
replaces characters that are not compatible with arcpy method, 
and finally renames them back to the original name of the corresponding images. 


"""



import os,arcpy


def create_shapefile(image_dir_path,shapefile_template):#creating empty polygon shapefiles from template
    for image in os.listdir(image_dir_path):
        image=image.replace("-","_").strip(".tif")#"-" character from image names incompatible with arcpy method below, have to temporarily switch to "_"
        arcpy.CopyFeatures_management(shapefile_template,image_dir_path+"/{}".format(image))
 


##!!!make sure to remove the created shapefiles in the table of contents before proceeding!!!



def rename_shapefiles(image_dir_path): #reverting shapefiles to original image names
    for shapefile in os.listdir(image_dir_path):
        rename=list(shapefile)
        rename[13]="-"
        rename[18]="-" #position 13 and 18 are where the "-" originally appeared in every image name
        rename="".join(rename)
        os.rename(os.path.join(image_dir_path,shapefile),os.path.join(image_dir_path,rename))




#Only tasks left to do are to set the appropriate XY coordinate system and import desired symbology.

 







