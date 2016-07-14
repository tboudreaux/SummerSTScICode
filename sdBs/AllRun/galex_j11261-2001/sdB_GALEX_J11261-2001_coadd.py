from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[171.544875,-20.026931],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J11261-2001/sdB_GALEX_J11261-2001_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J11261-2001/sdB_GALEX_J11261-2001_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
