from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[254.655958,38.796722], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ_165837.43+384748.2 /sdB_SDSSJ_165837.43+384748.2_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()