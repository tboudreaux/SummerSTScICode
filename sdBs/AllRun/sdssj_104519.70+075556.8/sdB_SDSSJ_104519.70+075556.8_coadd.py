from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[161.332083,7.932444],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_104519.70+075556.8/sdB_SDSSJ_104519.70+075556.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_104519.70+075556.8/sdB_SDSSJ_104519.70+075556.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
