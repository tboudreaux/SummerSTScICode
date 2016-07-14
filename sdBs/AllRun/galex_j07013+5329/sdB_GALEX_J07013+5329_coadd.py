from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[105.346292,53.494119],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J07013+5329/sdB_GALEX_J07013+5329_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J07013+5329/sdB_GALEX_J07013+5329_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
