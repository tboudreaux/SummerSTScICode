from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[335.4965,9.623805], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_LAMOST_J222159.16+093725.7 /sdB_LAMOST_J222159.16+093725.7_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
