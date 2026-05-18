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
# 🚢 Maritime AI Intelligence Platform 
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.4.0-F7931E.svg)](https://scikit-learn.org/)
[![GeoPandas](https://img.shields.io/badge/GeoPandas-0.14+-139C5A.svg)](https://geopandas.org/)

*A Unified Spatiotemporal and Stochastic Machine Learning Architecture for Maritime Traffic Network Resilience.*

## 📖 Overview
**Maritime-AI** is an end-to-end computational systems architecture designed to process gigabyte-scale Automatic Identification System (AIS) telemetry. By formalizing the analytical workflow as a deterministic mapping function $\mathcal{F} : X_{AIS} \rightarrow \{C, A, E, G\}$, this platform transforms noisy, non-stationary geodetic trajectories into actionable operational intelligence. 

Rather than treating machine learning, econometrics, environmental estimation, and graph theory as isolated computational layers, this architecture integrates them into a single deterministic intelligence pipeline.

## 🚀 Core Architectural Components

1. **Spatial Geofencing & Engineering (`The Masterpiece.py`)**
   * EPSG:4326 to EPSG:32617 Cartesian vector transformations for exact kinematic evaluation.
   * Spatial bounding and Boolean polygon intersections to reduce $\mathcal{O}(n^2)$ memory complexity.
2. **Supervised Vessel Classification (`The Random Forest Classifier.py`)**
   * Gini-optimized Random Forest ensemble predicting vessel typologies with **96% accuracy**.
   * Bypasses unverified AIS metadata by relying strictly on geometric and behavioral truth.
3. **Unsupervised Anomaly Isolation (`Anomaly Detection.py`)**
   * Isolation Forest architecture targeting "Dark Fleet" behavior and GPS spoofing.
   * Successfully flags physically implausible kinematics (e.g., cargo vessels spoofing 34+ knot velocities).
4. **Stochastic Congestion Forecasting (`The Logistics Layer.py`)**
   * Poisson Generalized Linear Model (GLM) for time-series infrastructure prediction.
   * Statistically evaluates (and rejects) assumed baseline congestion heuristics.
5. **Network Topology & Vulnerability (`Supply_Chain_Network.py`)**
   * Exact Eigenvector Centrality decomposition of regional supply chain trade routes.
   * Mathematically identifies critical load-bearing nodes and single-points-of-failure.
6. **Environmental ESG Intelligence (`Carbon_Emissions.py`)**
   * Spatially resolved carbon emission heuristics exposing extreme localized pollution asymmetries.

## 📂 Repository Structure
```text
adityaraprya/maritime-ai/
│
├── data/                       # (Ignored) Place your .gpkg and .tif data here
├── src/                        # Core algorithmic pipeline
│   ├── The Masterpiece.py             # Geospatial ingestion and geofencing
│   ├── The Random Forest Classifier.py # Supervised typological classification
│   ├── Anomaly Detection.py           # Unsupervised spatial security
│   ├── The Logistics Layer.py         # Poisson GLM econometrics
│   ├── Carbon_Emissions.py            # ESG physics heuristic
│   ├── Supply_Chain_Network.py        # Graph-theoretic centrality
│   └── Raster Heatmap.py              # Macro-scale density visualizations
│
├── dashboard/                  # UI and Interactive Elements
│   └── Build_Ultimate_Dashboard.py    # Compiles results into an executive HTML interface
│
├── requirements.txt            # System dependencies
├── LICENSE                     # MIT License
└── README.md                   # Project documentation
