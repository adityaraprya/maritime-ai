import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
from shapely.geometry import Polygon

# --- MACHINE LEARNING LIBRARIES ---
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

print("Initializing Phase 2: Machine Learning Classifier...")

# ==========================================
# 1. QUICK DATA PREP (From Phase 1)
# ==========================================
# (If running in the same notebook, you can skip to section 2)
port_coords = [(-80.130, 26.070), (-80.105, 26.070), (-80.105, 26.105), (-80.130, 26.105)]
port_geofence = Polygon(port_coords)
gdf = gpd.read_file('AISVesselTracks2025.gpkg', bbox=(-80.20, 26.05, -80.00, 26.15))
port_ships = gdf[gdf.geometry.intersects(port_geofence)].copy()

# ==========================================
# 2. FEATURE ENGINEERING & CLEANING
# ==========================================
print("\nPreparing features for the AI...")

# We select our predictors (Features) and our Target (Label)
features = ['Length', 'Width', 'Draft', 'DurationMinutes']
target = 'VesselGroup'

# Drop rows where ships forgot to broadcast their length or duration (NaNs)
ml_data = port_ships[features + [target]].dropna()

# Filter out rare classes so the AI has enough data to learn the main patterns
valid_classes = ['Pleasure Craft/Sailing', 'Cargo', 'Passenger', 'TugTow', 'Tanker']
ml_data = ml_data[ml_data[target].isin(valid_classes)]

X = ml_data[features]
y = ml_data[target]

# ==========================================
# 3. TRAIN / TEST SPLIT (Syllabus Unit 1)
# ==========================================
# We hide 20% of the data from the AI to test it on "unseen" ships later
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==========================================
# 4. TRAIN THE RANDOM FOREST (Syllabus Unit 2)
# ==========================================
print("\nTraining Random Forest Classifier on", len(X_train), "vessel tracks...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ==========================================
# 5. MODEL ASSESSMENT (Predictions & Evaluation)
# ==========================================
predictions = model.predict(X_test)

print("\n--- CLASSIFICATION REPORT ---")
# This shows Accuracy, Precision, and Recall
print(classification_report(y_test, predictions))

# --- VISUALIZATION 1: FEATURE IMPORTANCE ---
# Which variable was the most useful for the AI?
importance = pd.Series(model.feature_importances_, index=features).sort_values(ascending=False)

fig, axes = plt.subplots(1, 2, figsize=(15, 6))

sns.barplot(x=importance.values, y=importance.index, ax=axes[0], palette='viridis')
axes[0].set_title('What features does the AI look at?')
axes[0].set_xlabel('Importance Score')

# --- VISUALIZATION 2: CONFUSION MATRIX ---
# Where is the AI making mistakes?
cm = confusion_matrix(y_test, predictions, labels=model.classes_)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=model.classes_, yticklabels=model.classes_, ax=axes[1])
axes[1].set_title('Confusion Matrix (Actual vs Predicted)')
axes[1].set_ylabel('Actual Ship Type')
axes[1].set_xlabel('AI Predicted Ship Type')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()