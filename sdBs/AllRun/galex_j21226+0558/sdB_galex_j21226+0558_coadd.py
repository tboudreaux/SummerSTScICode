from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[320.668292,5.969114],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j21226+0558/sdB_galex_j21226+0558_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j21226+0558/sdB_galex_j21226+0558_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
