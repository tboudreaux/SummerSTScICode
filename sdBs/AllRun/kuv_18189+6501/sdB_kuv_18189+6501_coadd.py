from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[274.767542,65.035283],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kuv_18189+6501/sdB_kuv_18189+6501_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kuv_18189+6501/sdB_kuv_18189+6501_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
