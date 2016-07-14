from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[151.571875,-2.169056], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ910_100617.25-021008.6 /sdB_SDSSJ910_100617.25-021008.6_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
