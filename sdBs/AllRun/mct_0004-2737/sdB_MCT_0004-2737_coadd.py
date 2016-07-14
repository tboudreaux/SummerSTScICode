from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[1.692708,-27.348167],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_MCT_0004-2737/sdB_MCT_0004-2737_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_MCT_0004-2737/sdB_MCT_0004-2737_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
