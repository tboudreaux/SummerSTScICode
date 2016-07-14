from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[202.326875,-2.637997],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_LBQS_1326-0222/sdB_LBQS_1326-0222_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_LBQS_1326-0222/sdB_LBQS_1326-0222_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
