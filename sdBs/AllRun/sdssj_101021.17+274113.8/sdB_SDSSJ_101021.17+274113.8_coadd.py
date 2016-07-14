from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[152.588208,27.687167],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_101021.17+274113.8/sdB_SDSSJ_101021.17+274113.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_101021.17+274113.8/sdB_SDSSJ_101021.17+274113.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()