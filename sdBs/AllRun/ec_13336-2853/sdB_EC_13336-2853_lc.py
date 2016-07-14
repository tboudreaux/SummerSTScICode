from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[204.122917,-29.140903], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_EC_13336-2853 /sdB_EC_13336-2853_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
