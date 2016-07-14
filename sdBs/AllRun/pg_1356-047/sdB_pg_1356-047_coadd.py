from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[209.705833,-4.9633],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1356-047/sdB_pg_1356-047_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1356-047/sdB_pg_1356-047_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
