from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[208.913417,14.910825],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1353+152/sdB_pg_1353+152_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1353+152/sdB_pg_1353+152_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
