from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[185.341917,53.622667],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sbss_1218+538/sdB_sbss_1218+538_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sbss_1218+538/sdB_sbss_1218+538_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
