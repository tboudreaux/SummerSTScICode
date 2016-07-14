from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[108.956833,-54.132078],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J07158-5407/sdB_GALEX_J07158-5407_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J07158-5407/sdB_GALEX_J07158-5407_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
