from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[308.233292,77.955222],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_203255.99+775718.8/sdB_sdssj_203255.99+775718.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_203255.99+775718.8/sdB_sdssj_203255.99+775718.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
