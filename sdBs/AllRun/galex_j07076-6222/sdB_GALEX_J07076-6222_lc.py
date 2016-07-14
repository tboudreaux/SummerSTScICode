from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[106.912417,-62.378239], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_GALEX_J07076-6222 /sdB_GALEX_J07076-6222_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
