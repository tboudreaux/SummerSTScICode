from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[249.677917,22.687667], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ_163842.70+224115.6 /sdB_SDSSJ_163842.70+224115.6_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
