from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[144.543292,-3.999625], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_PG_0935-038 /sdB_PG_0935-038_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
