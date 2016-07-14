from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[19.870875,24.426606],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_0116+242/sdB_pg_0116+242_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_0116+242/sdB_pg_0116+242_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
