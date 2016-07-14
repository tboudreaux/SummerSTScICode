from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[46.955208,41.233778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_030749.25+411401.6/sdB_SDSSJ_030749.25+411401.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_030749.25+411401.6/sdB_SDSSJ_030749.25+411401.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
