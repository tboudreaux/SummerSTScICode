from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[268.082125,19.178389],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j17523+1910/sdB_galex_j17523+1910_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j17523+1910/sdB_galex_j17523+1910_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
