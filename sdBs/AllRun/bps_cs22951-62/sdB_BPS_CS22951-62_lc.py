from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[327.678167,-43.674542], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_BPS_CS22951-62 /sdB_BPS_CS22951-62_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
