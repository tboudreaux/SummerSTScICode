from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[252.230417,22.005694], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ910_164855.30+220020.5 /sdB_SDSSJ910_164855.30+220020.5_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()