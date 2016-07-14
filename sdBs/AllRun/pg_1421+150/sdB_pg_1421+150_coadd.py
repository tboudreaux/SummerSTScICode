from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[215.877917,14.808953],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1421+150/sdB_pg_1421+150_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1421+150/sdB_pg_1421+150_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
