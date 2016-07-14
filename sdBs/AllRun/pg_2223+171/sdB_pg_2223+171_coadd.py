from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[336.476417,17.386339],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_2223+171/sdB_pg_2223+171_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_2223+171/sdB_pg_2223+171_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
