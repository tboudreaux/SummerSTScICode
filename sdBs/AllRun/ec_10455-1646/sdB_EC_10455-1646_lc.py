from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[161.990667,-17.046228], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_EC_10455-1646 /sdB_EC_10455-1646_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
