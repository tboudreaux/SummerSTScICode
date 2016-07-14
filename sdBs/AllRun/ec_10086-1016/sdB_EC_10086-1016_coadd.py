from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[152.78325,-10.525756],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_EC_10086-1016/sdB_EC_10086-1016_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_EC_10086-1016/sdB_EC_10086-1016_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
