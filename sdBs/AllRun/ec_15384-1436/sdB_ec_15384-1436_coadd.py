from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[235.318375,-14.760633],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ec_15384-1436/sdB_ec_15384-1436_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ec_15384-1436/sdB_ec_15384-1436_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
