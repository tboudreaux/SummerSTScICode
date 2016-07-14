from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[168.591625,-24.358044],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J11143-2421/sdB_GALEX_J11143-2421_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J11143-2421/sdB_GALEX_J11143-2421_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
