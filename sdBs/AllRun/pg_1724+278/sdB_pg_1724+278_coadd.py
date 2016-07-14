from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[261.600292,27.738964],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1724+278/sdB_pg_1724+278_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1724+278/sdB_pg_1724+278_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
