# Field Fortifications in Ukraine - Dataset

This is a dataset which is an attempt to map field fortifications 
which have been constructed throughout the ongoing 
[Russo-Ukrainian War](https://en.wikipedia.org/wiki/Russo-Ukrainian_War).

### *This dataset is still incomplete and is actively being worked on.*

<br>

## Accessing the dataset

The data is stored in the form of Esri Shapefiles. 
These files can be found [here.](map_data/shp/fortifications_new/)

These are the fields defined in each dataset:

 - `misc.shp` - Misc fortifications.
 - - `type (char[10])`: The type of fortification.
 - `trenches.shp` - Trench lines and networks.
 - - `side (char[2])`: The side that controls the trench. 
 - - - `ua`: Trenches under Ukrainian control.
 - - - `ru`: Trenches under Russian control.
 - - - `??`: Trenches which is contested or whose status is unknown. 
 - `positions.shp` - Fortifications which are represented with points instead of lines.
 - - `type (char[80])`: The type of field position.
 - - - `revetment`: Vehicle shelters/revetments.
 - - - `emp`: Emplacements.
 - - - `dugout`: Dugouts and shelters.
 - - - For unknown/unspecified points, this value is NULL.

## TODO

 - [ ] Surovikin Line
 - - [x] Anti-tank ditches
 - - [x] Anti-tank obstacles
 - - [ ] Entrenchments
 - [ ] Redraw anti-tank ditches in Luhansk
 - [ ] Redraw and fix entrenchments in and around Krynky, Kherson Oblast
 - [ ] Split data into a vector tileset for release
