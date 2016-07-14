from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[248.735833,26.704639],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_163456.60+264216.7/sdB_SDSSJ910_163456.60+264216.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_163456.60+264216.7/sdB_SDSSJ910_163456.60+264216.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
