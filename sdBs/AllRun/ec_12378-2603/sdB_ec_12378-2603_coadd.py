from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[190.138542,-26.335725],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ec_12378-2603/sdB_ec_12378-2603_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ec_12378-2603/sdB_ec_12378-2603_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
