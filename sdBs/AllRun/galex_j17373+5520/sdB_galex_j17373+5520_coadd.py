from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[264.34925,55.3377],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j17373+5520/sdB_galex_j17373+5520_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j17373+5520/sdB_galex_j17373+5520_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
