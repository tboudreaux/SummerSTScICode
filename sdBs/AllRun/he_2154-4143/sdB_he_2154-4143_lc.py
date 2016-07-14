from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[329.508208,-41.480469], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_he_2154-4143/sdB_he_2154-4143_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
