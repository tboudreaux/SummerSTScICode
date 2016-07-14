from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[212.889375,70.626931],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j141133.45+703736.95/sdB_galex_j141133.45+703736.95_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j141133.45+703736.95/sdB_galex_j141133.45+703736.95_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
