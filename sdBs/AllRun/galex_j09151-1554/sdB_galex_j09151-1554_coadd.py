from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[138.783958,-15.910586],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j09151-1554/sdB_galex_j09151-1554_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j09151-1554/sdB_galex_j09151-1554_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
