from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[306.185458,-10.378617],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j20247-1022/sdB_galex_j20247-1022_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j20247-1022/sdB_galex_j20247-1022_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
