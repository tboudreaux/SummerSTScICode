from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[63.959208,1.905908],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J04158+0154/sdB_GALEX_J04158+0154_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J04158+0154/sdB_GALEX_J04158+0154_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
