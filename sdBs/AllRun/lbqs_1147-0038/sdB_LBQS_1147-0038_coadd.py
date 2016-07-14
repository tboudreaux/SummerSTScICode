from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[177.444167,0.915764],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_LBQS_1147-0038/sdB_LBQS_1147-0038_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_LBQS_1147-0038/sdB_LBQS_1147-0038_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
