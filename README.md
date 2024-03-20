# Field Fortifications in Ukraine - Dataset

This is a dataset which is an attempt to map field fortifications 
which have been constructed throughout the ongoing 
[Russo-Ukrainian War](https://en.wikipedia.org/wiki/Russo-Ukrainian_War).

### *This dataset is still incomplete and is actively being worked on.*

<br>

## Accessing the dataset

The data is stored in the form of Esri Shapefiles. 
These files can be found [here.](map_data/shp/fortifications/)

Each feature contains a `type` string field which denotes the type of fortification.

The fortification types are as follows:
 - `trench`: Field entrenchments.
 - `ditch`: Anti-tank ditches.
 - `teeth`: "Dragon's teeth" anti-tank obstacles.
 - `fp`: Emplacements / fighting positions.

**Disclaimer: Other attribute fields and fortification types may be added in the future.**

## TODO

 - [ ] Surovikin Line
 - - [x] Anti-tank ditches
 - - [ ] Anti-tank obstacles
 - - [ ] Entrenchments
 - [ ] Redraw anti-tank ditches in Luhansk
 - [ ] Split data into a vector tileset for release