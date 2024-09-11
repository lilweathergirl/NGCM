#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:27:37 2024

@author: ennisk
"""

import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Load the dataset
file_path = '/Users/ennisk/anaconda3/NGCM_ERA5_500mb_geopotential_comparison.nc'
ds = xr.open_dataset(file_path)

# Plotting setup
num_times = len(ds.time)
fig, axes = plt.subplots(
    nrows=num_times, ncols=2, figsize=(14,6 * num_times),
    subplot_kw={'projection': ccrs.PlateCarree()}
)

for i, time in enumerate(ds.time):
    for j, model in enumerate(ds.model):
        ax = axes[i, j]
        
        
        data = ds.geopotential.sel(time=time, model=model)
        geo_mb = data / 100
        
        
        im = geo_mb.plot(
            ax=ax, transform=ccrs.PlateCarree(), robust=True, cmap='coolwarm',
            x='longitude', y='latitude', add_colorbar=(j == 1), 
            cbar_kwargs={'orientation': 'horizontal', 'pad': 0.05} if j == 1 else None
        )
        
        
        ax.add_feature(cfeature.COASTLINE)
        ax.add_feature(cfeature.BORDERS)
        ax.add_feature(cfeature.STATES, edgecolor='black')
        ax.set_title(f'{model.values} - Time: {time.values}')
        ax.set_extent([190, 310, 15, 80], crs=ccrs.PlateCarree())  

fig.tight_layout()
#plt.savefig('/Users/ennisk/anaconda3/Figures/may2002_NGCM_ERA5.png', dpi=400)
plt.show()

# Loop through each forecast time and create a separate figure
for i, time in enumerate(ds.time):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6), subplot_kw={'projection': ccrs.PlateCarree()})

    for j, model in enumerate(ds.model):
        ax = axes[j]

        # Select the data for the current model and time
        data = ds.geopotential.sel(time=time, model=model)
        geo_mb = data / 100

        # Plotting the data with a coolwarm color map
        im = geo_mb.plot(
            ax=ax, transform=ccrs.PlateCarree(), robust=True, cmap='coolwarm',
            x='longitude', y='latitude', add_colorbar=True,
            cbar_kwargs={'orientation': 'horizontal', 'pad': 0.05}
        )

        # Adding map features
        ax.add_feature(cfeature.COASTLINE)
        ax.add_feature(cfeature.BORDERS)
        ax.add_feature(cfeature.STATES, edgecolor='black')
        ax.set_title(f'{model.values} - Time: {time.values}')
        ax.set_extent([190, 310, 15, 80], crs=ccrs.PlateCarree())

   
    fig.tight_layout()
    plt.savefig(f'forecast_time_{time.values}.png')
    plt.show()