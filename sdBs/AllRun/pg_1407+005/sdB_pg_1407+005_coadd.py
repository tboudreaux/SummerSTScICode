from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[212.586375,0.315167],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1407+005/sdB_pg_1407+005_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1407+005/sdB_pg_1407+005_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
