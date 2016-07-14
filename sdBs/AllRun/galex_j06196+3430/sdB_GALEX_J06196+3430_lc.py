from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[94.907542,34.508456], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_GALEX_J06196+3430 /sdB_GALEX_J06196+3430_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
