# Map_Generate
This repostory contains various python scripts fo getting marked maps

All of these scripts use the file gps.txt located in ~/.ros/router directory to get data for the markers. The file should have the following format

number of markers

Latitude1 Longitude1

Latitude2 Longitude2

.

.

.

You can also refer to the sample gps.txt present in this repository.

## bing_maps.py
This script generates a jpg map called map.jpg in the ~/.ros/router directory. The arguments it takes are-
* api_key : The bing API key to use with the REST Services
* center : The comma separated latitude and longitude of the center of the map
* pin_style : The style of the pins used to mark the maps. Please refer to [this link](https://docs.microsoft.com/en-us/bingmaps/rest-services/common-parameters-and-types/pushpin-syntax-and-icon-styles) to see the values for each pin style
* zoom : Zoom level of the map to be set
* size : Size of the map in pixels (height,width)

## folium_maps.py
This script generates a html map called map.html in the ~/.ros/router directory. The arguments it takes are-
* center : The comma separated latitude and longitude of the center of the map
* zoom : Zoom level of the map to be set

## gmplot_maps.py
This script generates a html map called map.html in the ~/.ros/router directory. The arguments it takes are-
* center : The comma separated latitude and longitude of the center of the map
* zoom : Zoom level of the map to be set
* size : Size of the marker to be used

## google_maps.py
This script generates a png map called map.png in the ~/.ros/router directory. The arguments it takes are-
* api_key : The google API key to use with the Google Cloud Platform
* center : The comma separated latitude and longitude of the center of the map
* zoom : Zoom level of the map to be set
* size : Size of the map in pixels (heightxwidth)
