from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[84.234625,39.921497],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j05369+3955/sdB_galex_j05369+3955_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j05369+3955/sdB_galex_j05369+3955_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
