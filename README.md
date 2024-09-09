This code provides the basic framework for running NeuralGCM.
ERA5 data on 37 pressure levels with inputs/outputs (on pressure levels): u_component_of_wind, v_component_of_wind, geopotential, temperature, specific_humidity, specific_cloud_ice_water_content, specific_cloud_liquid_water_content.
Forcings (surface level only): sea_surface_temperature, sea_ice_cover
Slice of ERA5 data is regridded to model resolution
By default the notebook uses intermediate deterministic NeuralGCM 1.4° model. 
Predictions are made for all variables on all pressure levels
At the end, you can compare outputs of NeuralGCM redictions to ERA5 reanalysis. 

Test code are some attempted changes to extract only 500 mb geoheight and an attempt at extracting surface pressure at a given location. 
