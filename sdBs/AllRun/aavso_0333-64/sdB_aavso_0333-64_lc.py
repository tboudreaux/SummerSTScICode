from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[53.642542,-64.015667], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_aavso_0333-64/sdB_aavso_0333-64_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
