from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[180.227917,-27.412569], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_EC_11583-2708 /sdB_EC_11583-2708_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
