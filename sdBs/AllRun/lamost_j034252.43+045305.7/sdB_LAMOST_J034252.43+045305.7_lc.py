from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[55.718458,4.884917], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_LAMOST_J034252.43+045305.7 /sdB_LAMOST_J034252.43+045305.7_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
