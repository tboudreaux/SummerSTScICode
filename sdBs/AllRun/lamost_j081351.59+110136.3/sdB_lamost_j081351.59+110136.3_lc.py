from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[123.464958,11.02675], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_lamost_j081351.59+110136.3/sdB_lamost_j081351.59+110136.3_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()