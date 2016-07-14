from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[280.687875,69.938989],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HS_1843+6953/sdB_HS_1843+6953_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HS_1843+6953/sdB_HS_1843+6953_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
