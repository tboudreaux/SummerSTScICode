from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[230.784583,-14.491203],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ec_15203-1418/sdB_ec_15203-1418_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ec_15203-1418/sdB_ec_15203-1418_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
