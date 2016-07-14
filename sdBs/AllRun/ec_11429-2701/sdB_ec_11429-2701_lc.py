from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[176.369167,-27.306356], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_ec_11429-2701/sdB_ec_11429-2701_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()