from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[199.820542,-18.831111], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_HE_1316-1834 /sdB_HE_1316-1834_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
