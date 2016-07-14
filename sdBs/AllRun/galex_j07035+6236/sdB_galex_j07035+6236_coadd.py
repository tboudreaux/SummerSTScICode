from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[105.881458,62.607231],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j07035+6236/sdB_galex_j07035+6236_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j07035+6236/sdB_galex_j07035+6236_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
