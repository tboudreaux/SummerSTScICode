from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[93.843125,62.714578],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j06153+6242/sdB_galex_j06153+6242_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j06153+6242/sdB_galex_j06153+6242_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
