from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[188.804375,10.499956],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_lbqs_1232+1046/sdB_lbqs_1232+1046_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_lbqs_1232+1046/sdB_lbqs_1232+1046_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
