from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[38.554958,23.703167], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_galex_j02342+2342/sdB_galex_j02342+2342_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
