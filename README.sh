#!/bin/bash
echo "TO RUN THE SASP INTERN 2016 SDB PULSATOR PIPELINE:"
echo "MCATMaker.py -> This generates a list of targets that gPhoton has data on from a list provided (that list muct be in the same director and formated correctly)"
echo "LMMaker.py -> This generates Count maps for all targets on the list generated by MCATMaker.py, this also generates default region files that can be used"
echo "AutoRegionMake.py -> This Attemptes to generate more target spesific region files using some very basic image analysis, these should still be looked at [CURRENTLY EXPERIMENAL]"
echo "CondorFilesMake.py -> This makes the nessesary files for the condor batch prossesing on the 64 code machine at STScI and dumps them into their target foldres"
echo "DynamicGAPCSVONLY.py -> This Generates the CSV data file from the returned gAperture data and dumps the files into the folders (used the list generated by MCATMaker.py)"
echo "GraphMake.py -> This used the CSV files generated by DynamicGAPCSVONLY.py and creates graphs for each vist to the target in each of them"
echo "HTMLMake.py -> Generates the nessesary HTML files for the pipeline quick look weberver"
echo "	HTMLMakePreTest.py -> version of HTMLMake.py with experimental featrures, this is the one usually run"
echo "An Apache server is running on port 5632 to allow for access to the data remototly over HTTP"
