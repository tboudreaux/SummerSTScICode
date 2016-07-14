from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[292.640625,-40.131653],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j19305-4007/sdB_galex_j19305-4007_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j19305-4007/sdB_galex_j19305-4007_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
