from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[23.91438,1.166369], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_LBQS_0003+0053 /sdB_LBQS_0003+0053_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
