from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[320.858917,83.564131], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_HS_2126+8320 /sdB_HS_2126+8320_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
