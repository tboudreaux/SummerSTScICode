from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[164.117417,55.920556],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sbss_1053+561/sdB_sbss_1053+561_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sbss_1053+561/sdB_sbss_1053+561_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
