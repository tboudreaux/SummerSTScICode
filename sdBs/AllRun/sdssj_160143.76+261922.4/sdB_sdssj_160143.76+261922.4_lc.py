from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[240.432333,26.322889], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj_160143.76+261922.4/sdB_sdssj_160143.76+261922.4_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
