from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[253.928417,13.030342],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1653+131/sdB_pg_1653+131_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1653+131/sdB_pg_1653+131_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
