from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[31.196292,27.484594], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_galex_j02047+2729/sdB_galex_j02047+2729_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
