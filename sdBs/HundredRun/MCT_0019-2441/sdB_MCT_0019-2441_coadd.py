from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[82.4175,-24.422506],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_MCT_0019-2441/sdB_MCT_0019-2441_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_MCT_0019-2441/sdB_MCT_0019-2441_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
