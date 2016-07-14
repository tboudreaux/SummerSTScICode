from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[164.354833,-45.820367],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J10574-4549/sdB_GALEX_J10574-4549_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J10574-4549/sdB_GALEX_J10574-4549_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()