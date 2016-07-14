from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[220.406083,0.090967],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_LBQS_1439+0007/sdB_LBQS_1439+0007_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_LBQS_1439+0007/sdB_LBQS_1439+0007_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
