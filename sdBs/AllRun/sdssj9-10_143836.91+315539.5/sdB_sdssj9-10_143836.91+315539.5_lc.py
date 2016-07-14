from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[219.653792,31.927639], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj9-10_143836.91+315539.5/sdB_sdssj9-10_143836.91+315539.5_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
