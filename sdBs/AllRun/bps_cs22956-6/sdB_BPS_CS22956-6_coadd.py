from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[325.832417,-65.830983],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_BPS_CS22956-6/sdB_BPS_CS22956-6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_BPS_CS22956-6/sdB_BPS_CS22956-6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
