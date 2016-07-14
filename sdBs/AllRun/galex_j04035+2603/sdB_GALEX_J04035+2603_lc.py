from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[60.894583,26.066511], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_GALEX_J04035+2603 /sdB_GALEX_J04035+2603_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
