from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[261.318542,52.240483],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1724+523/sdB_pg_1724+523_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1724+523/sdB_pg_1724+523_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
