from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[306.1705,13.624778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_202440.92+133729.2/sdB_sdssj_202440.92+133729.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_202440.92+133729.2/sdB_sdssj_202440.92+133729.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
