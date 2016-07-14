from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[152.393083,6.486333],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_100934.34+062910.8/sdB_SDSSJ_100934.34+062910.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_100934.34+062910.8/sdB_SDSSJ_100934.34+062910.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
