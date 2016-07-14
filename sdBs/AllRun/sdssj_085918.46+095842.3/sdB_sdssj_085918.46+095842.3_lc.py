from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[134.826917,9.978417], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj_085918.46+095842.3/sdB_sdssj_085918.46+095842.3_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
