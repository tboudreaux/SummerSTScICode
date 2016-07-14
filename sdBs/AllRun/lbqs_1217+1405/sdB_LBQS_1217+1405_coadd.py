from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[185.063208,13.819728],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_LBQS_1217+1405/sdB_LBQS_1217+1405_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_LBQS_1217+1405/sdB_LBQS_1217+1405_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
