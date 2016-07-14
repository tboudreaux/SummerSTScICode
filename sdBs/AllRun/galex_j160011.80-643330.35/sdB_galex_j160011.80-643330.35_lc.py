from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[240.049167,-64.558431], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_galex_j160011.80-643330.35/sdB_galex_j160011.80-643330.35_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
