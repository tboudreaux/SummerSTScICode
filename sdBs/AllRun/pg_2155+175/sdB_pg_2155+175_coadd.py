from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[329.454667,17.7143],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_2155+175/sdB_pg_2155+175_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_2155+175/sdB_pg_2155+175_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
