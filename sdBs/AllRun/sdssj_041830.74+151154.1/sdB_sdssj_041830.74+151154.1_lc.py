from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[64.628083,15.198361], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj_041830.74+151154.1/sdB_sdssj_041830.74+151154.1_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
