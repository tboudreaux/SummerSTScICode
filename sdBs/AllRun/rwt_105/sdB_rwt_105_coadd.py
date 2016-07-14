from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[67.801417,42.986256],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_rwt_105/sdB_rwt_105_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_rwt_105/sdB_rwt_105_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
