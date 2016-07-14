from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[48.874792,-59.567958],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J03154-5934/sdB_GALEX_J03154-5934_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J03154-5934/sdB_GALEX_J03154-5934_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
