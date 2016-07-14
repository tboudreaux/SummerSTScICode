from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[22.589625,7.061889], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj_013021.51+070342.8/sdB_sdssj_013021.51+070342.8_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
