from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[116.554833,33.552111], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ_074613.16+333307.6 /sdB_SDSSJ_074613.16+333307.6_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
