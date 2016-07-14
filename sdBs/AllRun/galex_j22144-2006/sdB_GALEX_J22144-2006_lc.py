from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[333.605167,-20.116639], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_GALEX_J22144-2006 /sdB_GALEX_J22144-2006_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
