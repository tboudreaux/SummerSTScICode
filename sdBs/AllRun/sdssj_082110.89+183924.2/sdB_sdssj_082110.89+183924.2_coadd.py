from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[125.295375,18.656722],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_082110.89+183924.2/sdB_sdssj_082110.89+183924.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_082110.89+183924.2/sdB_sdssj_082110.89+183924.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
