from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[345.641,26.049417], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_LAMOST_J230233.84+260257.9 /sdB_LAMOST_J230233.84+260257.9_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()