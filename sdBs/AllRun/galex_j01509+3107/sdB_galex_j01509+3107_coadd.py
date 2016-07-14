from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[27.726292,31.130497],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j01509+3107/sdB_galex_j01509+3107_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j01509+3107/sdB_galex_j01509+3107_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
