from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[29.132917,-13.907333],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_EC_01541-1409/sdB_EC_01541-1409_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_EC_01541-1409/sdB_EC_01541-1409_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
