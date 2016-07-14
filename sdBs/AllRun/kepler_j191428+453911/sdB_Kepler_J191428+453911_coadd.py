from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[288.616667,45.653056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_Kepler_J191428+453911/sdB_Kepler_J191428+453911_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_Kepler_J191428+453911/sdB_Kepler_J191428+453911_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
