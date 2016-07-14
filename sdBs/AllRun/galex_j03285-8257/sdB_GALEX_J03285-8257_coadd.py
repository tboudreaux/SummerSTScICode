from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[52.134667,-82.954383],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J03285-8257/sdB_GALEX_J03285-8257_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J03285-8257/sdB_GALEX_J03285-8257_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
