from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[285.760333,-35.4747],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J19030-3528/sdB_GALEX_J19030-3528_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J19030-3528/sdB_GALEX_J19030-3528_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
