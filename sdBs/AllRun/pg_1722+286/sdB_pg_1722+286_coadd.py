from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[261.049833,28.590806],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1722+286/sdB_pg_1722+286_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1722+286/sdB_pg_1722+286_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
