# 🚢 Maritime AI Intelligence Platform 
*A Unified Spatiotemporal and Stochastic Machine Learning Architecture for Maritime Traffic Network Resilience.*

### Overview
This repository contains the complete Python source code for an end-to-end maritime intelligence pipeline. It processes gigabyte-scale AIS telemetry to classify vessel typologies, isolate "Dark Fleet" anomalies, forecast port congestion, and map global supply chain vulnerabilities.

### Architecture Components
1. **Spatial Geofencing:** EPSG:4326 to EPSG:32617 Cartesian vector transformations.
2. **Supervised Classification:** Random Forest ensemble predicting vessel typologies (96% Accuracy).
3. **Unsupervised Security:** Isolation Forest anomaly detection for GPS spoofing and Dark Fleet identification.
4. **Econometrics:** Poisson Generalized Linear Model (GLM) for congestion forecasting.
5. **Graph Topology:** Eigenvector Centrality mapping of trade network bottlenecks.

### Execution Instructions
To run this pipeline locally:
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Download the MarineCadastre AIS dataset and place `.gpkg` and `.tif` files in the root directory.
4. Execute scripts sequentially (or run `Build_Ultimate_Dashboard.py` to generate the HTML UI).

### License
This project is licensed under the MIT License - see the LICENSE file for details.
