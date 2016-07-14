from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[329.131458,12.210444], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj_215631.55+121237.6/sdB_sdssj_215631.55+121237.6_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
