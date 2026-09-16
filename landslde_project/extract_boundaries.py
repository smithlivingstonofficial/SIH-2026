import geopandas as gpd
from pathlib import Path

# Project folder
project_folder = Path(
    "/Users/harishrajap/Documents/TakeYouForward/"
    "Landslide-predication-stage2/landslde_project"
)

# Input GADM GeoPackage
input_file = project_folder / "data/boundaries/gadm41_IND.gpkg"

# Output folder
output_folder = project_folder / "data/boundaries/states"
output_folder.mkdir(parents=True, exist_ok=True)

# Check input file
if not input_file.exists():
    raise FileNotFoundError(f"File not found: {input_file}")

# Check available layers
print("Reading GADM file...")
print(gpd.list_layers(input_file))

# Read state-level boundaries
gdf = gpd.read_file(input_file, layer="ADM_ADM_1")

print("\nAvailable state names:")
print(sorted(gdf["NAME_1"].unique()))

# Northeast Indian states
states = [
    "Assam",
    "Arunachal Pradesh",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Sikkim",
    "Tripura"
]

for state in states:
    state_gdf = gdf[gdf["NAME_1"] == state].copy()

    if state_gdf.empty:
        print(f"Not found: {state}")
        continue

    output_file = output_folder / f"{state.replace(' ', '_')}.geojson"

    state_gdf.to_file(
        output_file,
        driver="GeoJSON"
    )

    print(f"Saved: {output_file}")

print("\nDone.")