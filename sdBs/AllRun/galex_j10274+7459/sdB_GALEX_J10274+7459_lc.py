from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[156.870375,74.996444], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_GALEX_J10274+7459 /sdB_GALEX_J10274+7459_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
