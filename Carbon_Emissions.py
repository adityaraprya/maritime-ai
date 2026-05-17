import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

print("Step 1: Loading Track Data...")
florida_bbox = (-80.20, 26.05, -80.00, 26.45)
gdf = gpd.read_file('AISVesselTracks2025.gpkg', bbox=florida_bbox, layer='Atlantic_01')

print("Step 2: Calculating ESG Metrics (Carbon Physics)...")
# Drop rows without length or duration
gdf = gdf.dropna(subset=['Length', 'DurationMinutes']).copy()

# 1. Engine Power (kW) ~ Length (m) * 50 (Heuristic for educational purposes)
gdf['Estimated_Power_kW'] = gdf['Length'] * 50

# 2. Time in Hours
gdf['Duration_Hours'] = gdf['DurationMinutes'] / 60.0

# 3. CO2 Emissions (kg) = Power * Time * Emission Factor
gdf['CO2_Emissions_kg'] = gdf['Estimated_Power_kW'] * gdf['Duration_Hours'] * 0.6

# Convert to Metric Tons for readability
gdf['CO2_Emissions_Tons'] = gdf['CO2_Emissions_kg'] / 1000.0

print(f"\nTotal CO2 Emitted in this area (Jan 2025): {gdf['CO2_Emissions_Tons'].sum():,.2f} Metric Tons")

print("\nStep 3: Generating Pollution Spatial Map...")
# To map the pollution density, we extract the geometric center (centroid) of each voyage
gdf['centroid'] = gdf.geometry.centroid
gdf_points = gdf.set_geometry('centroid')

fig, ax = plt.subplots(figsize=(10, 8))
ax.set_facecolor('#00001a') # Dark background

# Scatter plot weighted by CO2 emissions
# We cap the maximum color threshold (vmax) at the 95th percentile so the ultra-polluters glow bright red!
scatter = ax.scatter(gdf_points.geometry.x, gdf_points.geometry.y,
                     c=gdf_points['CO2_Emissions_Tons'],
                     cmap='YlOrRd', # Yellow to Orange to Red
                     s=15, alpha=0.7,
                     vmin=0, vmax=gdf['CO2_Emissions_Tons'].quantile(0.95))

plt.colorbar(scatter, label='Estimated CO2 Emissions (Metric Tons)')
plt.title('Maritime ESG: Spatial Carbon Emissions Hotspots')

# Clean axes
ax.set_xticks([])
ax.set_yticks([])

plt.show()

print("\n--- TOP 5 HIGHEST EMITTING VESSELS ---")
top_polluters = gdf[['MMSI', 'VesselGroup', 'Length', 'Duration_Hours', 'CO2_Emissions_Tons']].sort_values(by='CO2_Emissions_Tons', ascending=False).head()
print(top_polluters)