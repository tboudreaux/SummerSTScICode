from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[174.921917,0.669047],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_lbqs_1137-0023/sdB_lbqs_1137-0023_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_lbqs_1137-0023/sdB_lbqs_1137-0023_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
