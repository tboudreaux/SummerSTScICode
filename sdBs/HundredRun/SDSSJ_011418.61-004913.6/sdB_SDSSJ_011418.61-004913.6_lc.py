from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[278.66313,0.820444], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ_011418.61-004913.6 /sdB_SDSSJ_011418.61-004913.6_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
