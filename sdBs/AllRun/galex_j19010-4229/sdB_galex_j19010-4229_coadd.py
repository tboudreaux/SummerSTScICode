from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[285.266958,-42.492644],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j19010-4229/sdB_galex_j19010-4229_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j19010-4229/sdB_galex_j19010-4229_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
