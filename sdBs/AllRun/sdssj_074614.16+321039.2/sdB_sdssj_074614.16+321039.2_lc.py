from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[116.559,32.177556], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj_074614.16+321039.2/sdB_sdssj_074614.16+321039.2_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
