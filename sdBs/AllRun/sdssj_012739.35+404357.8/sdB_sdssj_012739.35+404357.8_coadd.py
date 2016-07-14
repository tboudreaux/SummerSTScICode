from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[21.913958,40.732722],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_012739.35+404357.8/sdB_sdssj_012739.35+404357.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_012739.35+404357.8/sdB_sdssj_012739.35+404357.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
