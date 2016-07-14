from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[331.466208,-31.684825],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j22058-3141/sdB_galex_j22058-3141_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j22058-3141/sdB_galex_j22058-3141_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
