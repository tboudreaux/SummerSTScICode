from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[311.790083,12.170939],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j20471+1210/sdB_galex_j20471+1210_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j20471+1210/sdB_galex_j20471+1210_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
