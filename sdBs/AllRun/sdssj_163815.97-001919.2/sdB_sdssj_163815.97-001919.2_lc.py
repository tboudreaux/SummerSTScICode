from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[249.566542,0.322], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj_163815.97-001919.2/sdB_sdssj_163815.97-001919.2_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
