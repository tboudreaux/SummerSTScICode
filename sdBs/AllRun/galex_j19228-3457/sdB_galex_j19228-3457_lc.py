from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[290.7045,-34.958708], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_galex_j19228-3457/sdB_galex_j19228-3457_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
