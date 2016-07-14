from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[330.851958,37.829928],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J22034+3749/sdB_GALEX_J22034+3749_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J22034+3749/sdB_GALEX_J22034+3749_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
