from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[287.992125,-26.453336],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j19119-2627/sdB_galex_j19119-2627_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j19119-2627/sdB_galex_j19119-2627_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
