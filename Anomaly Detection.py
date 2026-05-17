import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
import numpy as np

print("Step 1: Loading Spatial Track Data...")
# Load the Florida coast data
florida_bbox = (-80.20, 26.05, -80.00, 26.45) 
# Note: Using layer='Atlantic_01' to suppress the warning
gdf = gpd.read_file('AISVesselTracks2025.gpkg', bbox=florida_bbox, layer='Atlantic_01')

print("Step 2: Engineering Security Features (Physics Engine)...")
# 1. We must drop tracks that have 0 minutes duration to avoid dividing by zero
gdf = gdf[gdf['DurationMinutes'] > 0].copy()

# 2. SPATIAL MATH: Calculate the physical distance of the track.
# EPSG:4326 is in degrees. We project to EPSG:32617 (UTM Zone 17N for Florida) to measure in exact meters.
gdf_projected = gdf.to_crs(epsg=32617)

# Calculate distance in Nautical Miles (1 NM = 1852 meters)
gdf['distance_nm'] = gdf_projected.geometry.length / 1852.0

# 3. Calculate Speed Over Ground (Knots) = Distance / Hours
gdf['calc_speed_knots'] = gdf['distance_nm'] / (gdf['DurationMinutes'] / 60.0)

# Filter out missing data for our ML model
features = ['calc_speed_knots', 'DurationMinutes', 'Length']
security_data = gdf.dropna(subset=features).copy()

print("Step 3: Deploying AI Anomaly Detector (Isolation Forest)...")
# Isolation Forest looks for data points that are mathematically "isolated" from normal traffic behavior
# contamination=0.02 means we are telling the AI: "Assume about 2% of these ships are acting suspiciously"
detector = IsolationForest(n_estimators=100, contamination=0.02, random_state=42)

# The AI returns -1 for Anomalies (Dark Fleet/Spoofers) and 1 for Normal Traffic
security_data['anomaly_score'] = detector.fit_predict(security_data[features])

# Separate the good actors from the bad actors
normal_traffic = security_data[security_data['anomaly_score'] == 1]
anomalies = security_data[security_data['anomaly_score'] == -1]

print(f"Total Tracks Analyzed: {len(security_data)}")
print(f"Normal Traffic: {len(normal_traffic)}")
print(f"CRITICAL ALERTS (Anomalies): {len(anomalies)}")

print("\nStep 4: Mapping the Dark Fleet...")
# ==========================================
# VISUALIZATION
# ==========================================
fig, ax = plt.subplots(figsize=(10, 8))

# Plot normal traffic in a faint, trusted blue
normal_traffic.plot(ax=ax, color='cyan', linewidth=0.5, alpha=0.3, label='Normal Traffic')

# Plot the anomalies in a bright, warning red
anomalies.plot(ax=ax, color='red', linewidth=2, alpha=0.9, label='Suspicious Activity (Anomalies)')

ax.set_facecolor('#00001a')
plt.title('Maritime Security: Dark Fleet & Spoofing Detection')
plt.legend()

# Turn off degree axes for a cleaner map
ax.set_xticks([])
ax.set_yticks([])

plt.show()

# Let's peek at WHY they were flagged
print("\n--- SAMPLE OF FLAGGED VESSELS ---")
print(anomalies[['MMSI', 'VesselGroup', 'Length', 'DurationMinutes', 'calc_speed_knots']].head())