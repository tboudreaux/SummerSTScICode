from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[50.662292,46.076144], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_KPD_0319+4553 /sdB_KPD_0319+4553_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
