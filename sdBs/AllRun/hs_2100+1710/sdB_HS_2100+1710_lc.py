from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[315.77225,17.376317], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_HS_2100+1710 /sdB_HS_2100+1710_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
