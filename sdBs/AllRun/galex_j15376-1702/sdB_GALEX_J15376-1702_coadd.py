from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[234.417917,-17.037508],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J15376-1702/sdB_GALEX_J15376-1702_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J15376-1702/sdB_GALEX_J15376-1702_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
