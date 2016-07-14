from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[329.519667,-4.677458], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_PB_7032 /sdB_PB_7032_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
