#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 10:27:01 2024

@author: ennisk
"""

import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature


# Load the datasets provided by the user
re_file_path = '/Users/ennisk/anaconda3/reanalysis_hour18/sfc_temp_18_20010810.nc'
forecast_file_path = '/Users/ennisk/anaconda3/Sfc_temp_LT1_10/tmp_2m_2001080100.nc'

# Load the reanalysis and forecast datasets
re_data = xr.open_dataset(re_file_path)
forecast_data = xr.open_dataset(forecast_file_path)

# Coordinates for Newark
Newark_coords = {'longitude': 285.82, 'latitude': 40.73}

# Extract temperature data for reanalysis
temperature_data = re_data['2t']
temperature_data = temperature_data.isel(height=0)  # Assuming one height level

Newark_temp_reanalysis = temperature_data.sel(
    lon=Newark_coords['longitude'],
    lat=Newark_coords['latitude'],
    method='nearest'
)

if 'time' in re_data.dims:
    specific_time = re_data.time.values[0]  # Select the first time value for reanalysis data
    Newark_temp_reanalysis = Newark_temp_reanalysis.sel(time=specific_time)

# Extract temperature data for forecast
temperature_forecast = forecast_data['2t']
temperature_forecast = temperature_forecast.isel(height=0)  # Assuming one height level

forecast_hour_time = '2001-08-10T00:00:00'
forecast_index = forecast_data['time'].to_index().get_loc(forecast_hour_time)  # Get the index for forecast time

# Selecting the forecast temperature for the desired forecast hour
forecast_hour_temp = temperature_forecast.isel(time=forecast_index)

Newark_temp_forecast = forecast_hour_temp.sel(
    lon=Newark_coords['longitude'],
    lat=Newark_coords['latitude'],
    method='nearest'
)

# Extract the temperature values
temp_value_reanalysis = Newark_temp_reanalysis.values.item()  
temp_value_forecast = Newark_temp_forecast.values.item()  

print(temp_value_reanalysis) 
print(temp_value_forecast)
