from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[288.7875,-29.053236],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J19151-2903/sdB_GALEX_J19151-2903_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J19151-2903/sdB_GALEX_J19151-2903_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
