from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[160.50325,-12.103131],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1039-118/sdB_pg_1039-118_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1039-118/sdB_pg_1039-118_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
