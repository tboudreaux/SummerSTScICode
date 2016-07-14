from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[288.988,62.099056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_191557.12+620556.6/sdB_sdssj_191557.12+620556.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_191557.12+620556.6/sdB_sdssj_191557.12+620556.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
