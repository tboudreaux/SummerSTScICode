from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[223.665833,19.616917],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1452+198/sdB_pg_1452+198_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1452+198/sdB_pg_1452+198_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
