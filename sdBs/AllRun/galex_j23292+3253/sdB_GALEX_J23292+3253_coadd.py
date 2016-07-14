from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[352.324375,32.896914],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J23292+3253/sdB_GALEX_J23292+3253_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J23292+3253/sdB_GALEX_J23292+3253_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
