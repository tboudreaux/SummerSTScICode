from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[192.630792,28.167792],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KUV_12481+2826/sdB_KUV_12481+2826_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KUV_12481+2826/sdB_KUV_12481+2826_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
