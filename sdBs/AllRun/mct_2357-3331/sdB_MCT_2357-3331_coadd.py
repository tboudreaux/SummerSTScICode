from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[0.083542,-33.249694],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_MCT_2357-3331/sdB_MCT_2357-3331_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_MCT_2357-3331/sdB_MCT_2357-3331_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
