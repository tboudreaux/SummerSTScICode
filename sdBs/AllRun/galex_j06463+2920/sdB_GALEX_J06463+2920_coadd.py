from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[101.57625,29.337058],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J06463+2920/sdB_GALEX_J06463+2920_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J06463+2920/sdB_GALEX_J06463+2920_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()