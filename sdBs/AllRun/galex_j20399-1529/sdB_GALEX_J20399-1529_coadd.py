from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[309.981583,-15.496489],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J20399-1529/sdB_GALEX_J20399-1529_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J20399-1529/sdB_GALEX_J20399-1529_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
