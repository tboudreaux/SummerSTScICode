from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[266.563875,40.318267],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J17462+4019/sdB_GALEX_J17462+4019_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J17462+4019/sdB_GALEX_J17462+4019_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
