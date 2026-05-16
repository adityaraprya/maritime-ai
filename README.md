# AI-Powered Maritime Intelligence System 🚢⚓

## Overview
An end-to-end geospatial intelligence pipeline that ingests gigabyte-scale Automatic Identification System (AIS) vessel trajectories, performs spatial intersection against operational geofences, and utilizes Machine Learning to automatically classify vessel types based on physical dimensions and behavioral movement patterns.

## 1. Problem Statement
Global maritime trade relies on the accurate tracking and classification of vessels. However, AIS transponders can be turned off (Dark Fleet behavior) or spoofed. This project builds a "White-Box" AI system capable of independently identifying a ship's class (Cargo, Tanker, Passenger, etc.) purely based on its radar-observable dimensions and dwell-time behavior within a specific port geofence.

## 2. Technical Stack
* **Geospatial Processing:** `GeoPandas`, `Rasterio`, `Shapely`, `PyProj`
* **Machine Learning:** `scikit-learn` (Random Forest, Classification Metrics)
* **Data Engineering:** `pandas`, `numpy`
* **Visualization:** `Folium` (Interactive Dashboards), `Matplotlib`, `Seaborn`

## 3. Methodology
The pipeline executes the following operational flow:
1. **Raster Heatmap Extraction:** Projected and downsampled massive `.tif` transit counts to identify macro-level shipping lanes.
2. **Vector Bounding & Spatial Filtering:** Used strict Bounding Boxes (`bbox`) to safely load gigabyte-scale `.gpkg` SQLite trajectory files without memory overload.
3. **Geofencing & Intersections:** Constructed `Shapely` polygons around Port Everglades and performed spatial intersections (`gdf.geometry.intersects()`) to filter out bypassing traffic and isolate anchored vessels.
4. **Feature Engineering:** Calculated `DurationMinutes` (Dwell Time) and aggregated physical features (`Length`, `Draft`, `Width`).
5. **Machine Learning:** Trained a Random Forest Classifier to separate the nonlinear spatial feature space.
6. **Operational Dashboard:** Generated an interactive `Folium` web map for decision support.

## 4. Results & Insights
* **Model Accuracy:** Achieved **96% Overall Accuracy** on the test set.
* **Feature Importance:** The AI identified `DurationMinutes` and `Length` as the most critical features for distinguishing vessel behavior.
* **Precision Targeting:** The model achieved a 0.98 F1-Score on Passenger (Cruise) ships due to their highly unique signature (massive length + very short port dwell times).

*(Insert screenshots of your Confusion Matrix, Feature Importance Bar Chart, and Folium Map here)*

## 5. Future Work
* **Live AIS Streaming:** Transitioning the ingestion pipeline from static `.gpkg` files to a real-time WebSocket/Kafka stream.
* **Bayesian Delay Forecasting:** Implementing hierarchical models (PyMC) to predict port congestion queues based on weather and seasonal traffic volume.
* **Graph Network Analysis:** Calculating Eigenvector Centrality across multiple global ports to identify supply chain single-points-of-failure.

## 6. How to Run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Download the 2025 AIS Track data from [NOAA MarineCadastre](https://hub.marinecadastre.gov/) and place it in the `/data/raw/` folder.
4. Run the pipeline scripts in the `/src/` directory.
