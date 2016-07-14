from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[112.197667,35.865994],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kuv_07255+3558/sdB_kuv_07255+3558_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kuv_07255+3558/sdB_kuv_07255+3558_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
