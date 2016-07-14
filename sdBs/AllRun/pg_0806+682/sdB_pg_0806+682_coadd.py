from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[122.984208,68.061967],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_0806+682/sdB_pg_0806+682_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_0806+682/sdB_pg_0806+682_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
