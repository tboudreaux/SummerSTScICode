from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[256.069333,64.85785],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J17042+6451/sdB_GALEX_J17042+6451_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J17042+6451/sdB_GALEX_J17042+6451_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
