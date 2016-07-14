from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[156.446042,0.483217],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_LBQS_1023+0044/sdB_LBQS_1023+0044_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_LBQS_1023+0044/sdB_LBQS_1023+0044_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
