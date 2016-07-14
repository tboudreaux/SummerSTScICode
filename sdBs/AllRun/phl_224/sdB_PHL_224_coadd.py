from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[334.993167,-8.638781],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PHL_224/sdB_PHL_224_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PHL_224/sdB_PHL_224_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()