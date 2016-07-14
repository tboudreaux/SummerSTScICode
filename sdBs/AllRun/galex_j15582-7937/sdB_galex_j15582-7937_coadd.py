from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[239.570458,-79.622125],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j15582-7937/sdB_galex_j15582-7937_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j15582-7937/sdB_galex_j15582-7937_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
