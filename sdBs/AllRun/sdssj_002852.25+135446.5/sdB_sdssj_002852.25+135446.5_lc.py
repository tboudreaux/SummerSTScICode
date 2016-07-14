from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[7.217708,13.912917], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj_002852.25+135446.5/sdB_sdssj_002852.25+135446.5_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
