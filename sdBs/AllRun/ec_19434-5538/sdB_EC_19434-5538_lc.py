from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[296.861542,-55.518431], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_EC_19434-5538 /sdB_EC_19434-5538_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
