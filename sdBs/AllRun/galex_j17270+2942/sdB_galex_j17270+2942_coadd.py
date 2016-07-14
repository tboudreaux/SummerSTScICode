from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[261.769417,29.708142],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j17270+2942/sdB_galex_j17270+2942_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j17270+2942/sdB_galex_j17270+2942_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
