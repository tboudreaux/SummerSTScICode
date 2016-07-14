from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[221.407375,-2.473569],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_lbqs_1443-0215/sdB_lbqs_1443-0215_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_lbqs_1443-0215/sdB_lbqs_1443-0215_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
