from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[301.728625,14.714936],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J20069+1442/sdB_GALEX_J20069+1442_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J20069+1442/sdB_GALEX_J20069+1442_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
