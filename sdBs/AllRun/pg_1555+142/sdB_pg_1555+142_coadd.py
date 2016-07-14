from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[239.494917,14.038925],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1555+142/sdB_pg_1555+142_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1555+142/sdB_pg_1555+142_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
