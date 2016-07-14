from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[28.296667,-39.071667],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_EC_01510-3919/sdB_EC_01510-3919_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_EC_01510-3919/sdB_EC_01510-3919_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
