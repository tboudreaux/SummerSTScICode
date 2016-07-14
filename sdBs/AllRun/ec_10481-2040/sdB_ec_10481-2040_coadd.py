from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[162.642667,-20.935267],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ec_10481-2040/sdB_ec_10481-2040_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ec_10481-2040/sdB_ec_10481-2040_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
