from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[341.979833,37.752139], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_fbs_2245+375/sdB_fbs_2245+375_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
