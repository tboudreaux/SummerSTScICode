from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[227.779542,17.537667],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1508+177/sdB_pg_1508+177_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1508+177/sdB_pg_1508+177_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
