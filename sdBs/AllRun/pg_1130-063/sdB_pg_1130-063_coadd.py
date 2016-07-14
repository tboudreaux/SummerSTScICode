from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[173.173333,-6.614617],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1130-063/sdB_pg_1130-063_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1130-063/sdB_pg_1130-063_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
