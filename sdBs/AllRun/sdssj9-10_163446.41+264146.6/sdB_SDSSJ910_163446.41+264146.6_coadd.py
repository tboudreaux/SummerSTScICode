from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[248.693375,26.696278],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_163446.41+264146.6/sdB_SDSSJ910_163446.41+264146.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_163446.41+264146.6/sdB_SDSSJ910_163446.41+264146.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
