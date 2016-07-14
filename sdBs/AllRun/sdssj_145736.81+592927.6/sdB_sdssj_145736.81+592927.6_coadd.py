from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[224.403375,59.491],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_145736.81+592927.6/sdB_sdssj_145736.81+592927.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_145736.81+592927.6/sdB_sdssj_145736.81+592927.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
