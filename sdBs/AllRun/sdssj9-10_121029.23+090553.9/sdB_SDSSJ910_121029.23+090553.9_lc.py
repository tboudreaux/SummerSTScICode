from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[182.621792,9.098306], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ910_121029.23+090553.9 /sdB_SDSSJ910_121029.23+090553.9_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
