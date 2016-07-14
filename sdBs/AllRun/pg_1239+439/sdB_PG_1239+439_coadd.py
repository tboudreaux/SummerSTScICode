from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[190.507417,43.673439],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1239+439/sdB_PG_1239+439_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1239+439/sdB_PG_1239+439_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
