import pandas as pd
import geopandas as gpd
import folium
from shapely.geometry import Polygon
from sklearn.ensemble import RandomForestClassifier

print("Step 1: Loading Spatial Data...")

# 1. LOAD AND GEOFENCE THE DATA
port_coords = [(-80.130, 26.070), (-80.105, 26.070), (-80.105, 26.105), (-80.130, 26.105)]
port_geofence = Polygon(port_coords)

# Note: We specify layer='Atlantic_01' to clear that warning you got earlier!
gdf = gpd.read_file('AISVesselTracks2025.gpkg', bbox=(-80.20, 26.05, -80.00, 26.15), layer='Atlantic_01')

# Filter for ships that entered the port
port_ships = gdf[gdf.geometry.intersects(port_geofence)].copy()

print("Step 2: Training the AI Model...")

# 2. TRAIN THE AI (So 'model' is defined)
features = ['Length', 'Width', 'Draft', 'DurationMinutes']
target = 'VesselGroup'
valid_classes = ['Pleasure Craft/Sailing', 'Cargo', 'Passenger', 'TugTow', 'Tanker']

# Clean data
ml_data = port_ships[features + [target] + ['MMSI', 'geometry']].dropna()
ml_data = ml_data[ml_data[target].isin(valid_classes)]

X = ml_data[features]
y = ml_data[target]

# Train the Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Generate Predictions for the dashboard
ml_data['Predicted_Class'] = model.predict(X)

print("Step 3: Generating Interactive Folium Dashboard...")

# 3. BUILD THE MAP
color_map = {
    'Pleasure Craft/Sailing': 'blue',
    'Cargo': 'orange',
    'Passenger': 'purple',
    'TugTow': 'darkgreen',
    'Tanker': 'red'
}

port_center = [26.085, -80.115]
m = folium.Map(location=port_center, zoom_start=13, tiles='CartoDB dark_matter')

# Draw the Geofence
folium_coords = [[lat, lon] for lon, lat in port_coords]
folium.Polygon(
    locations=folium_coords, color='lime', fill=True, fill_opacity=0.1,
    tooltip='Port Everglades Operational Geofence'
).add_to(m)

# Plot a sample of 300 ships so the HTML file doesn't lag your browser
sample_ships = ml_data.sample(n=min(300, len(ml_data)), random_state=42)

for idx, row in sample_ships.iterrows():
    geom = row['geometry']
    lines = [geom] if geom.geom_type == 'LineString' else geom.geoms
    
    for line in lines:
        track_coords = [[lat, lon] for lon, lat in line.coords]
        
        popup_html = f"""
        <b>MMSI:</b> {row['MMSI']}<br>
        <b>AI Prediction:</b> {row['Predicted_Class']}<br>
        <b>Actual Type:</b> {row['VesselGroup']}<br>
        <b>Length:</b> {row['Length']} meters<br>
        <b>Dwell Time:</b> {round(row['DurationMinutes']/60, 1)} hours
        """
        
        vessel_color = color_map.get(row['Predicted_Class'], 'white')
        
        folium.PolyLine(
            locations=track_coords,
            color=vessel_color,
            weight=2,
            opacity=0.7,
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=f"Predicted: {row['Predicted_Class']}"
        ).add_to(m)

output_file = "Port_Everglades_AI_Dashboard.html"
m.save(output_file)

print(f"\nSUCCESS! Dashboard saved as: {output_file}")
print("Double-click the HTML file to open it in your web browser.")