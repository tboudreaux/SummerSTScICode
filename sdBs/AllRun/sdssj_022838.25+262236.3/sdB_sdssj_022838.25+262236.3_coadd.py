from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[37.159375,26.37675],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_022838.25+262236.3/sdB_sdssj_022838.25+262236.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_022838.25+262236.3/sdB_sdssj_022838.25+262236.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
