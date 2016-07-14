from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[79.045125,-60.959894],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j05161-6057/sdB_galex_j05161-6057_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j05161-6057/sdB_galex_j05161-6057_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
