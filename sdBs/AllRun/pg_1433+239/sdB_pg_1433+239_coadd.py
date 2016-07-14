from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[218.834792,23.757639],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1433+239/sdB_pg_1433+239_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1433+239/sdB_pg_1433+239_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
