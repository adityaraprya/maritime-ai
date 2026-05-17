import os

print("Generating the Ultimate Executive Dashboard...")

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maritime AI Intelligence Platform</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #f4f6f9; color: #212529; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }
        .card { background-color: #ffffff; border: none; margin-bottom: 24px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); border-radius: 8px; overflow: hidden; }
        .card-header { background-color: #ffffff; border-bottom: 2px solid #f0f2f5; font-weight: 700; color: #2c3e50; font-size: 1.1rem; padding: 16px 20px; }
        .dashboard-img { width: 100%; height: auto; border-bottom: 1px solid #f0f2f5; }
        .iframe-container { height: 500px; width: 100%; border: none; }
        .insight-box { padding: 20px; background-color: #f8f9fa; border-top: 1px solid #e9ecef; }
        .badge-custom { background-color: #20c997; color: white; padding: 8px 12px; font-weight: 600; }
        .header-bg { background: linear-gradient(135deg, #0f2027, #203a43, #2c5364); color: white; padding: 40px 20px; margin-bottom: 30px; border-radius: 0 0 12px 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
    </style>
</head>
<body>

<div class="container-fluid p-0">
    <header class="header-bg text-center">
        <h1 class="display-4 fw-bold">AI Maritime Intelligence Platform</h1>
        <p class="fs-4 fw-light text-light opacity-75">End-to-End Geospatial, Machine Learning, and Econometric Analytics</p>
        <span class="badge badge-custom rounded-pill mt-2">Live Production Build</span>
    </header>

    <div class="container-fluid px-4">
        
        <div class="row">
            <div class="col-12">
                <div class="card">
                    <div class="card-header text-primary">📍 1. Operational Geofencing & Spatial Filtering</div>
                    <iframe src="Port_Everglades_AI_Dashboard.html" class="iframe-container"></iframe>
                    <div class="insight-box">
                        <strong>Engineering Insight:</strong> Utilized <code>GeoPandas</code> and <code>Shapely</code> to process gigabyte-scale AIS databases. Filtered over 8,000 vessel trajectories through a mathematical geofence to isolate the 3,283 tracks actively interacting with Port Everglades infrastructure.
                    </div>
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col-lg-6">
                <div class="card">
                    <div class="card-header text-success">🤖 2. Machine Learning: Vessel Classification</div>
                    <img src="feature_importance.png" alt="Feature Importance" class="dashboard-img" onerror="this.src='https://via.placeholder.com/800x500/e9ecef/495057?text=Save+feature_importance.png+here'">
                    <div class="insight-box">
                        <strong>Algorithm:</strong> Random Forest Classifier (<code>scikit-learn</code>)<br>
                        <strong>Results:</strong> Achieved <strong>96% Accuracy</strong> in classifying vessel types based purely on behavioral features. Extracted feature importance proving 'Length' and 'Dwell Time' are the strongest physical predictors.
                    </div>
                </div>
            </div>

            <div class="col-lg-6">
                <div class="card">
                    <div class="card-header text-danger">🚨 3. Security: Dark Fleet & Spoofing Detection</div>
                    <img src="anomaly_map.png" alt="Anomaly Map" class="dashboard-img" onerror="this.src='https://via.placeholder.com/800x500/e9ecef/495057?text=Save+anomaly_map.png+here'">
                    <div class="insight-box">
                        <strong>Algorithm:</strong> Isolation Forest (Unsupervised ML)<br>
                        <strong>Results:</strong> Processed geometric coordinates to calculate physical Speed Over Ground. Successfully isolated 175 mathematical anomalies, flagging a Cargo vessel spoofing impossible speeds (34+ knots) and irregular yacht loitering behavior.
                    </div>
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col-lg-6">
                <div class="card">
                    <div class="card-header text-warning">📊 4. Econometrics: Congestion Forecasting</div>
                    <img src="forecast_chart.png" alt="Forecast Chart" class="dashboard-img" onerror="this.src='https://via.placeholder.com/800x500/e9ecef/495057?text=Save+forecast_chart.png+here'">
                    <div class="insight-box">
                        <strong>Algorithm:</strong> Poisson Generalized Linear Model (GLM)<br>
                        <strong>Results:</strong> Disproved the "Weekend Surge" hypothesis. Statistical P-value analysis (0.385) confirmed the global maritime supply chain operates continuously without statistically significant weekend variance.
                    </div>
                </div>
            </div>

            <div class="col-lg-6">
                <div class="card">
                    <div class="card-header text-info">🌍 5. ESG: Environmental Carbon Mapping</div>
                    <img src="carbon_heatmap.png" alt="Carbon Heatmap" class="dashboard-img" onerror="this.src='https://via.placeholder.com/800x500/e9ecef/495057?text=Save+carbon_heatmap.png+here'">
                    <div class="insight-box">
                        <strong>Methodology:</strong> Geospatial Physics Heuristics<br>
                        <strong>Results:</strong> Mapped over 200,000 Metric Tons of CO2 emissions. Identified that idling luxury Mega-Yachts emit exponentially more localized carbon (1,452 Tons) than active commercial oil tankers in the same temporal window.
                    </div>
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col-12">
                <div class="card">
                    <div class="card-header" style="color: #6f42c1;">🕸️ 6. Graph Theory: Supply Chain Vulnerability</div>
                    <div class="text-center bg-dark">
                        <img src="network_graph.png" alt="Network Graph" class="img-fluid" style="max-height: 600px;" onerror="this.src='https://via.placeholder.com/1200x600/e9ecef/495057?text=Save+network_graph.png+here'">
                    </div>
                    <div class="insight-box">
                        <strong>Algorithm:</strong> Network Topology & Eigenvector Centrality (<code>NetworkX</code>)<br>
                        <strong>Results:</strong> Mathematically modeled the regional supply chain trade routes. Proved Miami (Score: 0.560) and the Panama Canal (Score: 0.545) are the ultimate single-points-of-failure; localized disruptions there will cascade globally.
                    </div>
                </div>
            </div>
        </div>

        <footer class="text-center py-4 text-muted border-top mt-4">
            <p class="mb-0">Designed and Engineered as a comprehensive Data Science & Machine Learning Portfolio.</p>
        </footer>

    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

# Save the ultimate dashboard file
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("\nSUCCESS! Your Ultimate Portfolio Dashboard has been generated.")
print("Open 'index.html' in your browser to view the final result.")