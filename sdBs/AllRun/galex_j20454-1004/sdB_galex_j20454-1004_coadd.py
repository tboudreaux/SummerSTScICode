from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[311.371667,-10.070978],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j20454-1004/sdB_galex_j20454-1004_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j20454-1004/sdB_galex_j20454-1004_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
