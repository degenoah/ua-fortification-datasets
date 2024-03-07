import os
import json
import simplekml
from datetime import datetime

def read_geojson_file(filename):
    with open(filename, "r") as f:
        geojson = json.load(f)
    
    return geojson

def create_fortification_layer(parent, dataset, features):
    match dataset["geotype"]:
        case "linestring":
            linestrings = []
            
            # Gather all of the separate multi-geometry lines into one array.
            for feature in features:
                for linestring in feature["geometry"]["coordinates"]:
                    ls_kml = []

                    for point in linestring:
                        ls_kml.append((point[0], point[1]))

                    linestrings.append(ls_kml)
            
            print(f"Creating layer: \"{dataset['name']}\"",
                f"({len(linestrings)} lines)")

            if "snippet" in dataset:
                parent.snippet.content = dataset["snippet"]["content"]

                parent.snippet.maxlines = 1 if "maxlines" not in dataset["snippet"] \
                                        else dataset["snippet"]["maxlines"]
            else:
                parent.snippet.content = f"Line Count: {len(linestrings)}"
                parent.snippet.maxlines = 1

            for linestring in linestrings:
                ls = parent.newlinestring(coords=linestring)

                ls.style.linestyle.width = dataset["width"]
                ls.style.linestyle.color = dataset["color"]
        case "polygon":
            pass # TODO

if __name__ == "__main__":
    kml = simplekml.Kml()
    
    kml.document.name = "Detailed Fortifications"
    kml.document.snippet.content = (
        "A detailed map of fortifications in Ukraine. " + 
        f"Last Updated: {datetime.today().strftime('%Y-%m-%d')}"
    )
    
    kml.document.description = ("<![CDATA[\n" +
        "<p>" + 
            "A detailed map of fortifications in the occupied territories of Ukraine. " +
            "Based off of satellite imagery from Planet, Maxar, and Copernicus, along " + 
            "with the previous works by Brady Africk and DeepStateUA." + 
        "</p>" + 
        
        "<p>" + 
            "<b>By:</b> Degenoah, Playfra, Clement, and AS-22." + 
        "</p>" + 
        
        f"<h6>KML build date: {datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}</h6>" +
    "]]>")

    datasets = [
        {
            "name": "Dragon's Teeth",
            "file": "../map_data/geojson/dragons_teeth.geojson",
            "color": "#ffc1c1c1",
            "width": 2.5,
        },
        {
            "name": "Anti-tank Ditches",
            "file": "../map_data/geojson/ditches.geojson",
            "color": "#ff7dff19",
            "width": 2.5,
        },
        {
            "name": "Trenches",
            "file": "../map_data/geojson/trenches_final.geojson",
            "color": "#ff14adff",
            "width": 1.5,
        },
        {
            "name": "Trenches (Secondary)",
            "snippet": {
                "content": "",
                "maxlines": 1
            },
            "file": "../map_data/geojson/treeline_entrenchments.geojson",
            "geotype": "linestring",
            "color": "#ffe629ff",
            "width": 1.5,
        },
    ]

    for dataset in datasets:
        # ignore any arguments that aren't files.
        if not os.path.isfile(dataset["file"]):
            continue

        dataset_data = read_geojson_file(dataset["file"])["features"]

        singlelayer = kml.newmultigeometry(name=dataset["name"])
        create_fortification_layer(singlelayer, dataset, dataset_data)

    kml.savekmz("fortifications.kmz")
    print("Written to fortifications.kmz")

