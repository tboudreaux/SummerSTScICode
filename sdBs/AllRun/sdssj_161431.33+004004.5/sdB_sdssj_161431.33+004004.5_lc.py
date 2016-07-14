from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[243.630542,0.667917], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj_161431.33+004004.5/sdB_sdssj_161431.33+004004.5_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
