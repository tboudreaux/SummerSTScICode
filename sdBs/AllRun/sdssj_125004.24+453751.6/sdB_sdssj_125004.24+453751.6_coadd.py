from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[192.517667,45.631],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_125004.24+453751.6/sdB_sdssj_125004.24+453751.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_125004.24+453751.6/sdB_sdssj_125004.24+453751.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
