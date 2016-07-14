from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[215.219375,-29.885397],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j14208-2953/sdB_galex_j14208-2953_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j14208-2953/sdB_galex_j14208-2953_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
