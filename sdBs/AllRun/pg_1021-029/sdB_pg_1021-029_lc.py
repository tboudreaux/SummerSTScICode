from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[156.075208,-3.177442], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_pg_1021-029/sdB_pg_1021-029_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
