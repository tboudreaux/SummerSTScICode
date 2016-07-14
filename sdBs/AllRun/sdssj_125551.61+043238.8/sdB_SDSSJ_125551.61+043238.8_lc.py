from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[193.965042,4.544111], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ_125551.61+043238.8 /sdB_SDSSJ_125551.61+043238.8_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
