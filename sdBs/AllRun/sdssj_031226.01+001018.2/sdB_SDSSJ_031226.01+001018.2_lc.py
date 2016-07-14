from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[48.108375,0.171722], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ_031226.01+001018.2 /sdB_SDSSJ_031226.01+001018.2_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()