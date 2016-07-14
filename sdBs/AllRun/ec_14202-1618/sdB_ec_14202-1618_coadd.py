from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[215.758292,-16.537717],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ec_14202-1618/sdB_ec_14202-1618_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ec_14202-1618/sdB_ec_14202-1618_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
