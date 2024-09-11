The NeuralGCM (inference_demo.py) code provides the basic framework for running the model.
Has data on 37 pressure levels with inputs/outputs including u wind, v wind, geopotential, temperature, specific humidity, spec. cloud-ice water content, spec. cloud liq water content.
Forcings (sfc): SST, sea ice cover. Slice of ERA5 data is regridded to model resolution.
I use the default intermediate deterministic NeuralGCM 1.4° model. 
Predictions can be made for all input/output variables above on all 37 pressure levels. 
You can compare outputs of NeuralGCM predictions to ERA5 reanalysis. 

Test codes are some attempted changes to extract only 500 mb geoheight and an attempt at extracting surface temperature at a given location. 
Demo geo is specifically for 500 mb geopotential height. 

