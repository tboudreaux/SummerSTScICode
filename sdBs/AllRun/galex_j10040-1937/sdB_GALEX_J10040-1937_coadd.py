from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[151.00325,-19.629614],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J10040-1937/sdB_GALEX_J10040-1937_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J10040-1937/sdB_GALEX_J10040-1937_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
