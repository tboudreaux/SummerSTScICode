from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[196.564958,48.838889],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1304+491/sdB_pg_1304+491_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1304+491/sdB_pg_1304+491_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
