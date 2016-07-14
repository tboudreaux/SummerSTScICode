from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[224.489292,-7.084714],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1455-069/sdB_pg_1455-069_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1455-069/sdB_pg_1455-069_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
