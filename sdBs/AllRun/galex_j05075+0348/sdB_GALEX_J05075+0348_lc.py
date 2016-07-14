from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[76.898875,3.80395], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_GALEX_J05075+0348 /sdB_GALEX_J05075+0348_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
