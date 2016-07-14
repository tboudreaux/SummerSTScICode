from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[151.430833,30.798831],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_CBS_19/sdB_CBS_19_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_CBS_19/sdB_CBS_19_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
