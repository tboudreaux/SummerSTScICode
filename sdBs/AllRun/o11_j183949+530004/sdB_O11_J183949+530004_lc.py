from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[279.954167,53.001111], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_O11_J183949+530004 /sdB_O11_J183949+530004_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
