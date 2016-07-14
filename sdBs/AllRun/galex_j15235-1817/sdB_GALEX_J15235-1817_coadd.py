from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[230.884208,-18.290625],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J15235-1817/sdB_GALEX_J15235-1817_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J15235-1817/sdB_GALEX_J15235-1817_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
