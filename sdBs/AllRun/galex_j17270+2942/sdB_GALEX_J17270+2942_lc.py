from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[261.769417,29.708142], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_GALEX_J17270+2942 /sdB_GALEX_J17270+2942_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
