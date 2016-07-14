from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[315.8855,30.594236],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j21035+3035/sdB_galex_j21035+3035_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j21035+3035/sdB_galex_j21035+3035_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()