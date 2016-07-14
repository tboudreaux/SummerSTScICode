from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[223.175167,52.617581],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1451+528/sdB_pg_1451+528_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1451+528/sdB_pg_1451+528_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
