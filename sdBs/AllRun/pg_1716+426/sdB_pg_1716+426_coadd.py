from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[259.515917,42.570453],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1716+426/sdB_pg_1716+426_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1716+426/sdB_pg_1716+426_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
