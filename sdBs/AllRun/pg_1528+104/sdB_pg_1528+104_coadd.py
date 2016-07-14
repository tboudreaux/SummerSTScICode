from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[232.793542,10.250431],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1528+104/sdB_pg_1528+104_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1528+104/sdB_pg_1528+104_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
