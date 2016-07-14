from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[209.696458,-27.538528], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_EC_13559-2717 /sdB_EC_13559-2717_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()