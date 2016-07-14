from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[232.048417,-7.275678], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_galex_j15281-0716/sdB_galex_j15281-0716_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
