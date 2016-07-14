from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[60.272125,-32.546114],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ec_03591-3232/sdB_ec_03591-3232_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ec_03591-3232/sdB_ec_03591-3232_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
