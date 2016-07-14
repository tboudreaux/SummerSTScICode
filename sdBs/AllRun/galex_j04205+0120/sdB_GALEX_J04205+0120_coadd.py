from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[65.145208,1.345056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J04205+0120/sdB_GALEX_J04205+0120_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J04205+0120/sdB_GALEX_J04205+0120_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
