from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[220.284958,1.172314],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_LBQS_1438+0123/sdB_LBQS_1438+0123_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_LBQS_1438+0123/sdB_LBQS_1438+0123_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
