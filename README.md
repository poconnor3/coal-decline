# The Change in Coal's Share of Electricity Generation in US States, 2001-2019

## Summary
Coal use has trended downwards lately in the US, largely attributed to a rise
in cheap natural gas and renewables. From 2001-2019, coal's share of total US
electricity generation has dropped by 54%. But has this decline happened evenly
 across the states? This repository contains a script to calculate the percent
 change of coal as a share of electricity generation by state from 2001-2019.
 Instructions are included to visualize this change in a map in QGIS.

## Input Data
One script (pct_change_coal.py) and one input csv (eia_variables.csv).

## Instructions
Part 1: Importing Data via API and Calculating Percent Change

1. Download an API key from the EIA, if you do not already have one. This can be done by accessing the following page on the EIA website: https://www.eia.gov/opendata/register.php

2. Download the eia_variables.csv and pct_change_coal.py files.

3. In the .py script, replace "YOUR_API_KEY" with your API key.

4. Run the script.

    1. The script will loop through each variable on the .csv and return the coal-powered and total electricity generation for each state, for each year between 2001-2019.

    2. The script then extracts the generation data from the metadata, and clips out all years other than 2001 and 2019.

    3. Next a MultiIndex is created by splitting the variable names on dashes ('-'), so that the fuel type (either coal ("COW") or total ("ALL"))

    4. New DataFrames are created for coal generation and total generation, then divided to find the share of coal generation for each state, in 2001 and 2019.

    5. A new DataFrame is created by calculating the percent change in the share of coal/total, from 2001-2019. This is exported to percent_change.csv.

5. Confirm that a percent_change.csv file was created.

Part 2: Visualizing the Data

1. Download a Shapefile of the US by state. The Census TIGER/Line Shapefiles are an appropriate choice, available at: https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html.

2. Import the Shapefile into QGIS. Set a reasonable map projection, like NAD 83 Conus Albers.

3. Import the percent_change.csv.

4. Run a spatial join on the Shapefile. Use percent_change as the join layer with field_1 as the join field and STUSPS as the target field.

5. Build a heat map. In the layer styling panel, choose Graduated Symbols and select percent_change_percent change in coal, 2001-2019. Choose an appropriate color ramp and use 5 equal interval classes.  

6. Export the map to a .png to see your results.

### Notes
1. The input .csv can be modified to include additional input variables. ELEC.GEN.ALL-NY-99.A is the variable representing total annual electricity generated in NY. The EIA database includes information about other generation sources, including renewables like wind and solar. For example, replacing "COW" with "WND" in the variable name will return total annual electricity generated by wind in NY. Replacing all the input "COW"s with "WND"s would created a script calculating the percent change in generation from wind in this same time period. More variables can be found at the EIA API webpage: https://www.eia.gov/opendata/qb.php

2. You may have noticed that Rhode Island and Vermont have been omitted. These states do not have coal reserves or coal plants, so the EIA has no data on coal generation for them. Massachusetts has also ended it's coal-powered electricity generation as of 2018.

3. Thank you Professor Wilcoxen for all your help with this project!
