from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[287.659792,-60.147331],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_NGC6752_3-118/sdB_NGC6752_3-118_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_NGC6752_3-118/sdB_NGC6752_3-118_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
