from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[82.254833,-56.552881],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J05290-5633/sdB_GALEX_J05290-5633_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J05290-5633/sdB_GALEX_J05290-5633_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()