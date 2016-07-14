from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[220.782083,9.526111], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj_144307.70+093134.0/sdB_sdssj_144307.70+093134.0_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
