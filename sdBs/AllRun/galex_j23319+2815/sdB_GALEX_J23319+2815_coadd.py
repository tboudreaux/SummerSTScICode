from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[352.995958,28.256206],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J23319+2815/sdB_GALEX_J23319+2815_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J23319+2815/sdB_GALEX_J23319+2815_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
