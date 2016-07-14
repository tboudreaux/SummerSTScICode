from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[359.593583,-32.077528],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_MCT_2355-3221/sdB_MCT_2355-3221_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_MCT_2355-3221/sdB_MCT_2355-3221_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
