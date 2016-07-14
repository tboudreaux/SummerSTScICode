from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[318.128833,-15.402881], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_galex_j211230.92-152410.37/sdB_galex_j211230.92-152410.37_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()