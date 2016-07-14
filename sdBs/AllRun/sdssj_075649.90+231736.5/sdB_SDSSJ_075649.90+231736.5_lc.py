from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[119.207917,23.293472], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ_075649.90+231736.5 /sdB_SDSSJ_075649.90+231736.5_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
