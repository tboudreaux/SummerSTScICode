from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[241.395667,6.459306], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ_160534.96+062733.5 /sdB_SDSSJ_160534.96+062733.5_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
