from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[358.401417,-36.505289], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_MCT_2351-3647 /sdB_MCT_2351-3647_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()