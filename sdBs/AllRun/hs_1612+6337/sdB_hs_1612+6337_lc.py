from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[243.264792,63.497042], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_hs_1612+6337/sdB_hs_1612+6337_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
