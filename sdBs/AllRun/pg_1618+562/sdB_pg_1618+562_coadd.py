from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[244.861542,56.099831],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1618+562/sdB_pg_1618+562_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1618+562/sdB_pg_1618+562_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
