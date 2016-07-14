from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[185.269083,-21.301528],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ec_12184-2101/sdB_ec_12184-2101_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ec_12184-2101/sdB_ec_12184-2101_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
