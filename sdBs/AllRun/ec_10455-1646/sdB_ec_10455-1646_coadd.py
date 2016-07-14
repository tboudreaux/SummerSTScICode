from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[161.990667,-17.046228],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ec_10455-1646/sdB_ec_10455-1646_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ec_10455-1646/sdB_ec_10455-1646_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
