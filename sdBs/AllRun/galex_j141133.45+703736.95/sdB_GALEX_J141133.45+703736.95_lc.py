from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[212.889375,70.626931], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_GALEX_J141133.45+703736.95 /sdB_GALEX_J141133.45+703736.95_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
