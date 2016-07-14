from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[163.855917,-8.346017],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1052-081/sdB_pg_1052-081_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1052-081/sdB_pg_1052-081_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
