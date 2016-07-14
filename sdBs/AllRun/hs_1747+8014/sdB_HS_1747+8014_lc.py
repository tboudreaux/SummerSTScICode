from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[265.788792,80.217881], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_HS_1747+8014 /sdB_HS_1747+8014_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
