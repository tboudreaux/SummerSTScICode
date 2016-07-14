from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[324.920417,0.174694], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj_213940.90-001028.9/sdB_sdssj_213940.90-001028.9_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
