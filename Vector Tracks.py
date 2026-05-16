import geopandas as gpd

print("Running spatial diagnostic on the GeoPackage...")

# We use rows=10 to safely peek inside without loading the whole file
gdf_sample = gpd.read_file('AISVesselTracks2025.gpkg', rows=10)

print(f"\n--- DIAGNOSTIC RESULTS ---")
print(f"1. Native Coordinate System (CRS): {gdf_sample.crs}")
print(f"2. Columns available: {gdf_sample.columns.tolist()}")
print(f"3. Sample Bounding Box (min_x, min_y, max_x, max_y): {gdf_sample.total_bounds}")

# Let's see the first 2 rows of actual data
print("\nFirst 2 rows of data:")
print(gdf_sample.head(2))