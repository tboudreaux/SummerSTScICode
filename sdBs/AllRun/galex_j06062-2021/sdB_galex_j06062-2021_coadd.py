from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[91.555583,-20.352019],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j06062-2021/sdB_galex_j06062-2021_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j06062-2021/sdB_galex_j06062-2021_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
