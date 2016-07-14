from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[65.010042,-54.070417],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j04200-5404/sdB_galex_j04200-5404_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j04200-5404/sdB_galex_j04200-5404_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
