from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[149.983417,35.666581],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_0956+359/sdB_pg_0956+359_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_0956+359/sdB_pg_0956+359_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
