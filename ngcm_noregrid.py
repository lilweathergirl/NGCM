#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 07:39:58 2024

@author: ennisk
"""

import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np

# Define the color bins and ticks for the color bar
color_bins = np.arange(-20, 41, 1)
ticks = [-20, -10, 0, 10, 20, 30, 40]

# Define the coordinates for the three locations
AR_coords = {'longitude': 267.72, 'latitude': 34.74}  # Little Rock, AR
LA_coords = {'longitude': 269.93, 'latitude': 29.95}  # New Orleans, LA
NC_coords = {'longitude': 277.45, 'latitude': 35.59}  # Asheville, NC


def plot_temp(file_path2, region='SE'):
    ds = xr.open_dataset(file_path2)
    time_index = 0
    print("Selected time:", ds.time.isel(time=time_index).values)

    if region == 'NH':
        projection = ccrs.NorthPolarStereo(central_longitude=-100)
        extent = [-180, 180, 20, 90]
    elif region == 'NA':
        projection = ccrs.PlateCarree()
        extent = [190, 310, 15, 80]
    elif region == 'NAm':
        projection = ccrs.PlateCarree()
        extent = [260, 295, 30, 55]
    elif region == 'SE':
        projection = ccrs.PlateCarree()
        extent = [260, 290, 25, 40]
        
    temp_data = ds.temperature.isel(time=time_index)
    temp_c = temp_data - 273.15  # Convert from Kelvin to Celsius
    
    plt.figure(figsize=(10, 8))
    ax = plt.axes(projection=projection)
    ax.set_extent(extent, crs=ccrs.PlateCarree())
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.add_feature(cfeature.STATES, linestyle=':')
    
    temp_plot = temp_c.T.plot.contourf(
        ax=ax, cmap='coolwarm', extend='both', levels=color_bins, add_colorbar=False
    )
    
    # Set up the color bar with custom ticks
    cbar = plt.colorbar(temp_plot, ax=ax, orientation='vertical', pad=0.05)
    cbar.set_ticks(ticks)
    cbar.set_label('Temperature (°C)')
    
    # Extract temperatures at specified coordinates using the correct dimension names
    temp_AR = temp_c.sel(longitude=AR_coords['longitude'], latitude=AR_coords['latitude'], method='nearest')
    temp_LA = temp_c.sel(longitude=LA_coords['longitude'], latitude=LA_coords['latitude'], method='nearest')
    temp_NC = temp_c.sel(longitude=NC_coords['longitude'], latitude=NC_coords['latitude'], method='nearest')
    
    
    print(f"NGCM Temperature at Little Rock, AR: {temp_AR.values:.2f} °C")
    print(f"NGCM Temperature at New Orleans, LA: {temp_LA.values:.2f} °C")
    print(f"NGCM Temperature at Asheville, NC: {temp_NC.values:.2f} °C")
    
    ax.scatter(
       [AR_coords['longitude'], LA_coords['longitude'], NC_coords['longitude']],
       [AR_coords['latitude'], LA_coords['latitude'], NC_coords['latitude']],
       color='cyan', zorder=5, transform=ccrs.PlateCarree()
   )
    
    
    ax.set_title('NGCM Temperature 08/03/2011')
    plt.show()

file_path = '/Users/ennisk/anaconda3/NGCM_aug2011_temp.nc'
plot_temp(file_path, region='SE')
    
    
    
    
    