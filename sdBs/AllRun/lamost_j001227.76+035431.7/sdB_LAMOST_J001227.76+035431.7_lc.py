from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[3.115667,3.908806], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_LAMOST_J001227.76+035431.7 /sdB_LAMOST_J001227.76+035431.7_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
