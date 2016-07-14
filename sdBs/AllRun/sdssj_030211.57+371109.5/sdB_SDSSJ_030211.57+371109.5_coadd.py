from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[45.548208,37.185972],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_030211.57+371109.5/sdB_SDSSJ_030211.57+371109.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_030211.57+371109.5/sdB_SDSSJ_030211.57+371109.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
