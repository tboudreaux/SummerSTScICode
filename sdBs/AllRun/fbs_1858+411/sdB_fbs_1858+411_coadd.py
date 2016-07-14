from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[285.115583,41.251278],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_1858+411/sdB_fbs_1858+411_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_1858+411/sdB_fbs_1858+411_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
