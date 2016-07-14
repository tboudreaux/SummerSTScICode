from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[101.572042,43.611056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_0642+436/sdB_fbs_0642+436_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_0642+436/sdB_fbs_0642+436_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
