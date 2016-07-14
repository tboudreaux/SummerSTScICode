from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[290.483833,37.98975],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_192156.12+375923.1/sdB_sdssj_192156.12+375923.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_192156.12+375923.1/sdB_sdssj_192156.12+375923.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
