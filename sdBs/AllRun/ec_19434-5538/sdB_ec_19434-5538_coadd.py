from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[296.861542,-55.518431],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ec_19434-5538/sdB_ec_19434-5538_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ec_19434-5538/sdB_ec_19434-5538_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
