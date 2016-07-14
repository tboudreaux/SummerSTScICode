from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[234.997917,16.852222], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ910_J153959.50+165108.0 /sdB_SDSSJ910_J153959.50+165108.0_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
