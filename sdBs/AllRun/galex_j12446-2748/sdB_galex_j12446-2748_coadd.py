from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[191.173625,-27.815975],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j12446-2748/sdB_galex_j12446-2748_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j12446-2748/sdB_galex_j12446-2748_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()