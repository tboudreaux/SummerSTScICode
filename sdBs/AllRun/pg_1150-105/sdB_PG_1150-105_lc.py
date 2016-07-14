from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[178.369208,-10.778314], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_PG_1150-105 /sdB_PG_1150-105_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
