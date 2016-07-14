from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[125.318958,-8.473006], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_GALEX_J08212-0828 /sdB_GALEX_J08212-0828_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
