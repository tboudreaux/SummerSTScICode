from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[252.591792,31.463822],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1648+315/sdB_pg_1648+315_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1648+315/sdB_pg_1648+315_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
