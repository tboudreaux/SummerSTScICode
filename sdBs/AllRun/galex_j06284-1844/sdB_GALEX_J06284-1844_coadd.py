from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[97.10675,-18.748144],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J06284-1844/sdB_GALEX_J06284-1844_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J06284-1844/sdB_GALEX_J06284-1844_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
