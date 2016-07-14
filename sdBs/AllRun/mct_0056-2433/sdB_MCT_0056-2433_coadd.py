from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[14.790083,-24.291317],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_MCT_0056-2433/sdB_MCT_0056-2433_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_MCT_0056-2433/sdB_MCT_0056-2433_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
