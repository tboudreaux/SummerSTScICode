from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[334.836125,39.767639],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_221920.67+394603.5/sdB_SDSSJ_221920.67+394603.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_221920.67+394603.5/sdB_SDSSJ_221920.67+394603.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
