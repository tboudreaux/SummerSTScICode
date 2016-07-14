from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[262.070292,7.810833],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_172816.87+074839.0/sdB_sdssj_172816.87+074839.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_172816.87+074839.0/sdB_sdssj_172816.87+074839.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
