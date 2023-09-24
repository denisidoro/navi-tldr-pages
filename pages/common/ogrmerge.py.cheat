; This has been extracted from
; https://github.com/tldr-pages/tldr/blob/master/pages/common/ogrmerge.py.md

% ogrmerge.py, common

# Create a GeoPackage with a layer for each input Shapefile
ogrmerge.py -f <GPKG> -o <path_to_output.gpkg> <path_to_input1.shp path_to_input2.shp ...>

# Create a virtual datasource (VRT) with a layer for each input GeoJSON
ogrmerge.py -f <VRT> -o <path_to_output.vrt> <path_to_input1.geojson path_to_input2.geojson ...>

# Concatenate two vector datasets and store source name of dataset in attribute 'source_name'
ogrmerge.py -single -f <GeoJSON> -o <path_to_output.geojson> -src_layer_field_name country <source_name> <path_to_input1.shp path_to_input2.shp ...>
