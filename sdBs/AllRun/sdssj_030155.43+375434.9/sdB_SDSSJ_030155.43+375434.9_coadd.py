from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[45.480958,37.909694],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_030155.43+375434.9/sdB_SDSSJ_030155.43+375434.9_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_030155.43+375434.9/sdB_SDSSJ_030155.43+375434.9_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
