from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[97.974208,0.320206], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_KPD_0629-0016 /sdB_KPD_0629-0016_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
