from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[249.883958,23.380222], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ910_163932.15+232248.8 /sdB_SDSSJ910_163932.15+232248.8_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
