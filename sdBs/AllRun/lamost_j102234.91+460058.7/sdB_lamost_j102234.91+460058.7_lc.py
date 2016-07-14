from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[155.645458,46.016306], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_lamost_j102234.91+460058.7/sdB_lamost_j102234.91+460058.7_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
