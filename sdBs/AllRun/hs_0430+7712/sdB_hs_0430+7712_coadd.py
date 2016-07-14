from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[69.300917,77.302406],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_hs_0430+7712/sdB_hs_0430+7712_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_hs_0430+7712/sdB_hs_0430+7712_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
