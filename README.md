The NeuralGCM (inference_demo.py) code provides the basic framework for running the model.
Has data on 37 pressure levels with inputs/outputs including u wind, v wind, geopotential, temperature, specific humidity, spec. cloud-ice water content, spec. cloud liq water content.
Forcings (sfc): SST, sea ice cover. Slice of ERA5 data is regridded to model resolution.
The three deterministic NeuralGCM's vary in model resolution. (0.7°, 1.4°, and 2.8°). 
Predictions can be made for all input/output variables on all 37 pressure levels. 
You can compare NeuralGCM predictions to ERA5 reanalysis. 

Test code are some random changes I initially made when first running the model. 
Demo geo is specifically for extracting 500 mb geopotential height hindcasts and reanalysis data at NeuralGCM's native grid resolution.  
Demo kelsey is for regridding NeuralGCM predictions to 0.25°x 0.25° to be able to compare NeuralGCM output to other model outputs (i.e., GraphCast). 



