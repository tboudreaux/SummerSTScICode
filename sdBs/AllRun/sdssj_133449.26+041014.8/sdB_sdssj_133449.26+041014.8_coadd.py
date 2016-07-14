from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[203.70525,4.170778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_133449.26+041014.8/sdB_sdssj_133449.26+041014.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_133449.26+041014.8/sdB_sdssj_133449.26+041014.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
