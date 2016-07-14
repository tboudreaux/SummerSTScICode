from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[61.40313,-36.473478],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_MCT_0013-3645/sdB_MCT_0013-3645_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_MCT_0013-3645/sdB_MCT_0013-3645_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
