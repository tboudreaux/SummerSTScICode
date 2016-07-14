from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[227.501875,44.134603],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1508+443/sdB_pg_1508+443_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1508+443/sdB_pg_1508+443_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
