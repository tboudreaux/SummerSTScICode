from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[17.552667,-14.132492],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_MCT_0107-1423/sdB_MCT_0107-1423_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_MCT_0107-1423/sdB_MCT_0107-1423_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
