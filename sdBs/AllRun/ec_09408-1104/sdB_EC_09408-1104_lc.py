from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[145.814833,-11.297778], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_EC_09408-1104 /sdB_EC_09408-1104_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
