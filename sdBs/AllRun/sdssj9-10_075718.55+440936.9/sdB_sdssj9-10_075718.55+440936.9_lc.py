from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[119.327292,44.16025], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj9-10_075718.55+440936.9/sdB_sdssj9-10_075718.55+440936.9_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
