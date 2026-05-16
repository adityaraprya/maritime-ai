import geopandas as gpd
from shapely.geometry import Polygon
import matplotlib.pyplot as plt

# 1. DEFINE THE GEOFENCE (Port Everglades / Fort Lauderdale)
# These coordinates form a rough box around the actual docking areas
port_coords = [
    (-80.130, 26.070), # Bottom-Left
    (-80.105, 26.070), # Bottom-Right
    (-80.105, 26.105), # Top-Right
    (-80.130, 26.105)  # Top-Left
]
port_geofence = Polygon(port_coords)

# 2. LOAD THE DATA (Florida Coast Bounding Box)
florida_bbox = (-80.20, 26.05, -80.00, 26.15)
print("Loading vector tracks...")
gdf = gpd.read_file('AISVesselTracks2025.gpkg', bbox=florida_bbox)

# 3. SPATIAL FILTERING (The Magic Step)
# We ask GeoPandas: Which of these ship tracks actually touch our Port Polygon?
print("Filtering for ships that entered the port...")
gdf['entered_port'] = gdf.geometry.intersects(port_geofence)

# Create a new dataframe with ONLY the ships that went inside the port
port_ships = gdf[gdf['entered_port'] == True].copy()

print(f"Total ships in area: {len(gdf)}")
print(f"Ships that actually entered Port Everglades: {len(port_ships)}")

# 4. STATISTICAL AGGREGATION (Prepping for your ML/Stats units)
# Let's see what TYPES of ships are entering and how long they stay
if len(port_ships) > 0:
    stats = port_ships.groupby('VesselGroup').agg(
        total_visits=('MMSI', 'count'),
        avg_duration_minutes=('DurationMinutes', 'mean'),
        avg_length=('Length', 'mean')
    ).round(2).sort_values(by='total_visits', ascending=False)
    
    print("\n--- Port Everglades Traffic Stats ---")
    print(stats)
else:
    print("\nNo ships found inside the geofence. We may need to adjust the coordinates!")

# 5. VISUALIZE THE INTERSECTION
fig, ax = plt.subplots(figsize=(10, 8))

# Plot all ships in faint blue
gdf.plot(ax=ax, linewidth=0.5, alpha=0.3, color='blue', label='Bypassing Ships')

# Plot the ships that entered the port in bright red!
port_ships.plot(ax=ax, linewidth=1.5, alpha=0.8, color='red', label='Port Traffic')

# Plot the Geofence boundary in green
gpd.GeoSeries([port_geofence]).boundary.plot(ax=ax, color='lime', linewidth=2)

ax.set_facecolor('#00001a')
plt.title('Port Everglades: Spatial Intersection Analysis')
plt.show()