from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[283.074292,-21.797617],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J18522-2147/sdB_GALEX_J18522-2147_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J18522-2147/sdB_GALEX_J18522-2147_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
