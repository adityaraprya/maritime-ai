import pandas as pd
import geopandas as gpd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from shapely.geometry import Polygon

print("Step 1: Loading & Filtering Spatial Data...")
florida_bbox = (-80.20, 26.05, -80.00, 26.45)
port_coords = [(-80.130, 26.070), (-80.105, 26.070), (-80.105, 26.105), (-80.130, 26.105)]
port_geofence = Polygon(port_coords)

# Load data and filter for ships inside Port Everglades
gdf = gpd.read_file('AISVesselTracks2025.gpkg', bbox=florida_bbox, layer='Atlantic_01')
port_ships = gdf[gdf.geometry.intersects(port_geofence)].copy()

print("Step 2: Time-Series Feature Engineering...")
# 1. Extract the exact Date the ship arrived
port_ships['ArrivalDate'] = pd.to_datetime(port_ships['TrackStartTime']).dt.date

# 2. Count how many ships arrived each day
daily_counts = port_ships.groupby('ArrivalDate').size().reset_index(name='Daily_Arrivals')
daily_counts['ArrivalDate'] = pd.to_datetime(daily_counts['ArrivalDate'])

# 3. Create Econometric Features
daily_counts['DayOfWeek'] = daily_counts['ArrivalDate'].dt.dayofweek
# Create a binary variable: 1 if Saturday/Sunday, 0 if Weekday
daily_counts['Is_Weekend'] = daily_counts['DayOfWeek'].apply(lambda x: 1 if x >= 5 else 0)

# We must add a 'constant' (intercept) for statsmodels to calculate the baseline traffic
X = sm.add_constant(daily_counts[['Is_Weekend']])
y = daily_counts['Daily_Arrivals']

print("Step 3: Training Poisson GLM...")
# Train the Poisson model (Link function is inherently Logarithmic)
poisson_model = sm.GLM(y, X, family=sm.families.Poisson())
results = poisson_model.fit()

print("\n" + "="*50)
print("POISSON REGRESSION ECONOMETRICS")
print("="*50)
print(results.summary())
print("="*50)

print("\nStep 4: Forecasting & Visualization...")
# Generate predictions using our fitted model
daily_counts['Predicted_Arrivals'] = results.predict(X)

# Plot Actual Traffic vs Model Predictions
fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(daily_counts['ArrivalDate'], daily_counts['Daily_Arrivals'], 
       label='Actual Daily Arrivals', alpha=0.6, color='#4A90E2')

ax.plot(daily_counts['ArrivalDate'], daily_counts['Predicted_Arrivals'], 
        color='#E94A4A', marker='o', linewidth=3, label='Poisson GLM Forecast')

ax.set_facecolor('#f4f6f9')
plt.title('Port Everglades: Daily Congestion Forecasting', fontsize=14, fontweight='bold')
plt.xlabel('Date')
plt.ylabel('Number of Ships Arriving')
plt.legend()
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()