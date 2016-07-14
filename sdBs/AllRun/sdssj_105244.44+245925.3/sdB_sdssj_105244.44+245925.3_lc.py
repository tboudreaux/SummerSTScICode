from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[163.185167,24.990361], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj_105244.44+245925.3/sdB_sdssj_105244.44+245925.3_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
