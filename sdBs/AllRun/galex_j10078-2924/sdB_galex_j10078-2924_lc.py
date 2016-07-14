from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[151.966167,-29.409347], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_galex_j10078-2924/sdB_galex_j10078-2924_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
