from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[247.398875,52.931831],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1628+530/sdB_pg_1628+530_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1628+530/sdB_pg_1628+530_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
