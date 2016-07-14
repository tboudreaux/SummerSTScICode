from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[315.132125,14.870489],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J21005+1452/sdB_GALEX_J21005+1452_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J21005+1452/sdB_GALEX_J21005+1452_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()