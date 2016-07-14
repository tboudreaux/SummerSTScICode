from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[345.810083,39.429053],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J23032+3925/sdB_GALEX_J23032+3925_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J23032+3925/sdB_GALEX_J23032+3925_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
