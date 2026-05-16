import os
import rasterio

# 1. Point the environment specifically to RASTERIO's bundled PROJ directory
rasterio_proj_dir = os.path.join(os.path.dirname(rasterio.__file__), 'proj_data')
os.environ["PROJ_LIB"] = rasterio_proj_dir
os.environ["PROJ_DATA"] = rasterio_proj_dir

from rasterio.windows import from_bounds
from rasterio.warp import transform_bounds
import matplotlib.pyplot as plt

# Our Lat/Lon bounding box for Port of LA (EPSG:4326)
la_bbox_wgs84 = (-118.30, 33.65, -118.15, 33.80)

print("Initializing Rasterio Environment...")

# 2. Use rasterio.Env() to safely lock in the internal C-libraries
with rasterio.Env():
    with rasterio.open('ais-transit-count-2025.tif') as src:
        print(f"The raster's native CRS is: {src.crs}")
        
        # TRANSLATE: Convert our Lat/Lon box into the raster's native coordinate system
        projected_bounds = transform_bounds(
            'EPSG:4326',  
            src.crs,      
            *la_bbox_wgs84
        )
        
        print(f"Translated bounding box: {projected_bounds}")
        
        # CROP & READ
        window = from_bounds(*projected_bounds, transform=src.transform)
        data = src.read(1, window=window)
        
        # PLOT
        fig, ax = plt.subplots(figsize=(10, 8))
        extent = (projected_bounds[0], projected_bounds[2], projected_bounds[1], projected_bounds[3]) 
        
        im = ax.imshow(data, cmap='inferno', extent=extent, vmax=data.max() * 0.5)
        plt.colorbar(im, ax=ax, label='Transit Count')
        plt.title('Port of LA Transit Counts (Corrected CRS)')
        
        ax.set_xticks([])
        ax.set_yticks([])
        
        plt.show()