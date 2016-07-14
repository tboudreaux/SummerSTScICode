from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[222.70625,62.828],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_145049.50+624940.8/sdB_SDSSJ_145049.50+624940.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_145049.50+624940.8/sdB_SDSSJ_145049.50+624940.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
