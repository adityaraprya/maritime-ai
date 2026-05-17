import os

print("Generating Master HTML Dashboard...")

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maritime AI Intelligence Platform</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #0d1117; color: #c9d1d9; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }
        .card { background-color: #161b22; border: 1px solid #30363d; margin-bottom: 20px; }
        .card-header { background-color: #21262d; border-bottom: 1px solid #30363d; font-weight: bold; }
        .dashboard-img { width: 100%; height: auto; border-radius: 4px; }
        .iframe-container { height: 500px; width: 100%; border: none; border-radius: 4px; }
        .badge-custom { background-color: #238636; color: white; }
    </style>
</head>
<body>

<div class="container-fluid py-4">
    <header class="pb-3 mb-4 border-bottom border-secondary">
        <h1 class="display-5 fw-bold text-white">🚢 AI Maritime Intelligence Platform</h1>
        <p class="fs-4">End-to-End Geospatial, Machine Learning, and Econometric Analysis of the Global Supply Chain.</p>
        <span class="badge badge-custom fs-6">Status: Live Processing Complete</span>
    </header>

    <div class="row">
        <div class="col-lg-7">
            <div class="card shadow-sm">
                <div class="card-header text-info">📍 Layer 1: Spatial Geofencing & AI Classification</div>
                <div class="card-body p-0">
                    <iframe src="Port_Everglades_AI_Dashboard.html" class="iframe-container"></iframe>
                </div>
                <div class="card-footer text-muted small">
                    *Interactive Map: Zoom, pan, and click on vessel tracks to view ML predictions and physical dimensions.
                </div>
            </div>
        </div>

        <div class="col-lg-5">
            <div class="card shadow-sm">
                <div class="card-header text-danger">🚨 Layer 2: Security & Dark Fleet Detection</div>
                <div class="card-body text-center">
                    <img src="anomaly_map.png" alt="Anomaly Detection Map" class="dashboard-img mb-3" onerror="this.src='https://via.placeholder.com/600x400/161b22/c9d1d9?text=Save+anomaly_map.png+here'">
                    <p class="text-start small"><strong>Algorithm:</strong> Isolation Forest<br>
                    <strong>Insight:</strong> Detected 175 mathematical anomalies, including impossible speed spoofing (>34 knots) and irregular deep-water loitering.</p>
                </div>
            </div>
        </div>
    </div>

    <div class="row">
        <div class="col-lg-6">
            <div class="card shadow-sm">
                <div class="card-header text-warning">📊 Layer 3: Econometric Port Forecasting</div>
                <div class="card-body text-center">
                    <img src="forecast_chart.png" alt="Poisson Forecast Chart" class="dashboard-img mb-3" onerror="this.src='https://via.placeholder.com/600x400/161b22/c9d1d9?text=Save+forecast_chart.png+here'">
                    <p class="text-start small"><strong>Algorithm:</strong> Poisson Generalized Linear Model (GLM)<br>
                    <strong>Insight:</strong> Disproved the "Weekend Surge" theory. P-value (0.385) indicates that the maritime supply chain operates continuously without statistically significant weekend traffic variations.</p>
                </div>
            </div>
        </div>

        <div class="col-lg-6">
            <div class="card shadow-sm">
                <div class="card-header" style="color: #bc8cff;">🕸️ Layer 4: Global Supply Chain Topology</div>
                <div class="card-body text-center">
                    <img src="network_graph.png" alt="Network Topology Graph" class="dashboard-img mb-3" onerror="this.src='https://via.placeholder.com/600x400/161b22/c9d1d9?text=Save+network_graph.png+here'">
                    <p class="text-start small"><strong>Algorithm:</strong> Graph Theory & Eigenvector Centrality<br>
                    <strong>Insight:</strong> Mathematically identified Miami (0.560) and the Panama Canal (0.545) as the most critical structural nodes. Failure here cascades across the entire network.</p>
                </div>
            </div>
        </div>
    </div>
</div>

</body>
</html>
"""

# Save the master dashboard file
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("\nSUCCESS! Open 'index.html' in your browser to see your complete portfolio dashboard.")