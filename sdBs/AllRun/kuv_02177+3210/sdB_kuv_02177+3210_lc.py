from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[35.166292,32.39585], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_kuv_02177+3210/sdB_kuv_02177+3210_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
