from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[208.894917,16.004806],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1353+162/sdB_pg_1353+162_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1353+162/sdB_pg_1353+162_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
