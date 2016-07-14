from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[331.0505,26.418928], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_hs_2201+2610/sdB_hs_2201+2610_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
