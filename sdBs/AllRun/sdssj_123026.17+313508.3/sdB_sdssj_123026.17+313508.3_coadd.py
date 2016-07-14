from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[187.609042,31.585639],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_123026.17+313508.3/sdB_sdssj_123026.17+313508.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_123026.17+313508.3/sdB_sdssj_123026.17+313508.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
