from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[313.337708,-40.107483],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J205321.05-400626.94/sdB_GALEX_J205321.05-400626.94_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J205321.05-400626.94/sdB_GALEX_J205321.05-400626.94_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
