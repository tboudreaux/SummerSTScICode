from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[221.7805,-3.041353],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_LBQS_1444-0249/sdB_LBQS_1444-0249_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_LBQS_1444-0249/sdB_LBQS_1444-0249_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
