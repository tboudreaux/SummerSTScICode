from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[286.068708,-35.850647],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j19042-3551/sdB_galex_j19042-3551_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j19042-3551/sdB_galex_j19042-3551_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
