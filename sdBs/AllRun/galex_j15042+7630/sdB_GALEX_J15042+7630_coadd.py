from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[226.051458,76.512994],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J15042+7630/sdB_GALEX_J15042+7630_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J15042+7630/sdB_GALEX_J15042+7630_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
