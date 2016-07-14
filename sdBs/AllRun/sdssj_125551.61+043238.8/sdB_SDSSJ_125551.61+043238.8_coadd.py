from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[193.965042,4.544111],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_125551.61+043238.8/sdB_SDSSJ_125551.61+043238.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_125551.61+043238.8/sdB_SDSSJ_125551.61+043238.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
