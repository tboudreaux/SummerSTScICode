from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[239.742542,21.974775], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_KUV_15568+2207 /sdB_KUV_15568+2207_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()