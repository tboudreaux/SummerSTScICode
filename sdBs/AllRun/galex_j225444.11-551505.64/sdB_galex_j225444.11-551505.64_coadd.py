from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[343.683792,-55.251567],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j225444.11-551505.64/sdB_galex_j225444.11-551505.64_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j225444.11-551505.64/sdB_galex_j225444.11-551505.64_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
