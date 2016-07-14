from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[193.034792,11.851036], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_GALEX_J12521+1151 /sdB_GALEX_J12521+1151_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
