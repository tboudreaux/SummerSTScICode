from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[193.60563,-30.715608],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_MCT_0049-3059/sdB_MCT_0049-3059_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_MCT_0049-3059/sdB_MCT_0049-3059_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
