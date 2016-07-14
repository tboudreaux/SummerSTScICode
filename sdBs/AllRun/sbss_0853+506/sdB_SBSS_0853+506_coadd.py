from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[134.143917,50.463556],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SBSS_0853+506/sdB_SBSS_0853+506_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SBSS_0853+506/sdB_SBSS_0853+506_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
