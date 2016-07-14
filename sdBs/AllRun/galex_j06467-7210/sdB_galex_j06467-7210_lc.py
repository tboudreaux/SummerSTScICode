from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[101.682958,-72.176803], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_galex_j06467-7210/sdB_galex_j06467-7210_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
