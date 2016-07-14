from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[317.09925,24.810883],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j21083+2448/sdB_galex_j21083+2448_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j21083+2448/sdB_galex_j21083+2448_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
