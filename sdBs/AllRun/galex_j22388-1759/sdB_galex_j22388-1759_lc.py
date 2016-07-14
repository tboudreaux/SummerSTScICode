from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[339.71425,-17.987844], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_galex_j22388-1759/sdB_galex_j22388-1759_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
