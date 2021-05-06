# Goe-spatial Data

## Metadata
____
Metadata of spatial data should have the same name as the file and needs to be 
stored in the same directory to open properly in a GIS (e.g. ISO 19115 or XML 
format).
The proposed [Metadata](https://www.fgdc.gov/metadata/csdgm/00.html) structure 
by FGDC suggests the following components to be included in the metadata:
> Identification_Information +
> 
> 0{Data_Quality_Information}1 + 
> 
> 0{Spatial_Data_Organization_Information}1 + 
> 
> 0{Spatial_Reference_Information}1 +
> 
> 0{Entity_and_Attribute_Information}1 +
> 
> 0{Distribution_Information}n +
> 
> Metadata_Reference_Information

iGIS group requires the provided baseline data to
include the following metadata features:
* Names of the researchers
* Data collection methods
* Date of data acquisition
* Processing steps (Methods)
* Processing tools
* Parameters used
* Paper reference
* Description on the channels (bands)


## Formatting
____
### Spatial Reference:
Spatial data should be in [California Albers, NAD83 projection](https://spatialreference.org/ref/epsg/3310/)

### Raster Data
* Co-registered, geo-referenced raster
* No data: -9999
* Bands should be described in the metadata
* Data reference, data collection methods, processing methods, codes that read 
  the data should be mentioned in the metadata
* No spaces or special characters (except an underscore _ ) should be used in 
  the attributes
* Field names should not exceed 13 characters
* Total length for the file and its path should not exceed 128 characters

### Vector Data
* Co-registered, geo-referenced vector
* No spaces or special characters (except an underscore _ ) should be used in 
  the attributes
* The length of shapefile names should not exceed 10 characters

## Geographic Extent
The extent of (raw) data should be larger than the study area, we recommentd a buffer of at least 10km for the (raw) data. This improves the accuracy of characteristics that rely on the neighboring areas such as distance and density. A shapefile of the extent of this project is available [here](./Extent). The map of the study area of foresite project can be found in [this](./AB2551) directory.

