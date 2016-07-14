from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[119.636917,9.611117],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J07585+0936/sdB_GALEX_J07585+0936_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J07585+0936/sdB_GALEX_J07585+0936_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
