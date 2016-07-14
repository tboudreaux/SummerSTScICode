from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[324.378917,22.319389],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j21375+2219/sdB_galex_j21375+2219_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j21375+2219/sdB_galex_j21375+2219_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()