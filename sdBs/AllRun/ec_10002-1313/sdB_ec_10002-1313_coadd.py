from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[150.657917,-13.460547],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ec_10002-1313/sdB_ec_10002-1313_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ec_10002-1313/sdB_ec_10002-1313_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
