from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[216.202667,-19.083692],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ec_14220-1851/sdB_ec_14220-1851_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ec_14220-1851/sdB_ec_14220-1851_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
