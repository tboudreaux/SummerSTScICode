from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[285.904167,38.603611], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_kepler_j19036+3836/sdB_kepler_j19036+3836_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
